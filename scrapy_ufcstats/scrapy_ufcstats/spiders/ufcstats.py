# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from ..items import ScrapyUfcstatsItem
from datetime import datetime
import pendulum
import re


class UfcstatsSpider(Spider):
    name = 'fights'

    def extract_number_of(self, stat_string):
        pre_of = int(re.sub('[^0-9]', '', stat_string.split('of')[0]))
        post_of = int(re.sub('[^0-9]', '', stat_string.split('of')[1]))
        return(pre_of, post_of)

    def start_requests(self):
        urls = [
            'http://www.ufcstats.com/statistics/events/completed?page=all'
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        # Finds all event_urls that have already occured.
        for event_url in response.css('.b-link_style_black::attr(href)').getall():
            yield Request(event_url, callback=self.parse_event)


    # Splits the text with of into two numeric values so that it easier to manipulate.
    def split_of_text(self, of_string):
        landed_string = int(re.sub('[^0-9]', '', of_string.split('of')[0]))
        attempted_string = int(re.sub('[^0-9]', '', of_string.split('of')[1]))
        return(landed_string, attempted_string)


    def parse_event(self, response):
        # Appends date.
        date = response.xpath("//section[@class='b-statistics__section_details']//li[1]").get().split()[-4:-1]
        # Type converts from 'July 27, 2019' format date to datetime object.
        date = pendulum.datetime(int(date[2]),
                                 datetime.strptime(date[0], '%B').month,
                                 int(re.sub("[^0-9]", "", date[1])))

        # Appends location.
        location = response.xpath("//section[@class='b-statistics__section_details']//"
                                  "li[2]").get().split("</i>\n\n")[1].replace('\n', '').replace('</li>', '').strip()

        # Appends attendance.
        attendance = response.xpath("//section[@class='b-statistics__section_details']"
                                    "//li[3]").get().split("Attendance:\n      </i>\n")[1].replace('\n    </li>',
                                                                                                   '').strip()
        # Changes the type from string numeric e.g. '10,513' to int.
        attendance = attendance.replace(',','')

        # Fetches all fight urls from each event.
        for fight_url in response.css('a.b-flag_style_green::attr(href)').getall():
            yield Request(fight_url,
                          callback=self.parse_fight,
                          meta={'date': date, 'location': location, 'attendance': attendance})


    def parse_fight(self, response):
        # Initalizes items to add the scraped data into.
        items = ScrapyUfcstatsItem()

        # Extract url data from response.
        items['url'] = response.url

        # Extracts meta data from previous parsing layer.
        items['date'] = response.meta['date']
        items['location'] = response.meta['location']
        items['attendance'] = response.meta['attendance']

        # Extracts fighter name.
        fighters = response.xpath("//h3[@class='b-fight-details__person-name']//a/text()").extract()
        if len(fighters) == 0:
            fighters = response.xpath("//h3[@class='b-fight-details__person-name']/span/text()").extract()

        # Extracts fighter nicknames.
        nicknames = response.xpath("//p[@class='b-fight-details__person-title']/text()").extract()

        # Data wrangles names.
        items['fighter_1'] = fighters[0].strip()
        items['fighter_1_nn'] = nicknames[0].strip()
        items['fighter_2'] = fighters[1].strip()
        items['fighter_2_nn'] = nicknames[1].strip()

        # Extracts who won the fight.
        fighter_1_outcome = response.xpath("//body[@class='b-page']/section[@class='b-statistics__section_details']"
                                           "/div[@class='l-page__container']/div[@class='b-fight-details']"
                                           "/div[@class='b-fight-details__persons clearfix']"
                                           "/div[1]/i/text()").extract()
        fighter_1_outcome = fighter_1_outcome[0].strip()
        if fighter_1_outcome == "W":
            items['winner']  = items['fighter_1']
        else:
            items['winner']  = items['fighter_2']

        # Extracts the winning method.
        items['win_method'] = response.xpath("//body[@class='b-page']/section[@class='b-statistics__section_details']"
                              "/div[@class='l-page__container']/div[@class='b-fight-details']"
                              "/div[@class='b-fight-details__fight']/div[@class='b-fight-details__content']/p[1]/i[1]"
                              "/i[2]/text()").extract()[0].strip()


        # Extracts number of rounds fought.
        rounds = response.xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[2]/p[1]/i[2]").get()
        # Data wrangles rounds by getting rid of all non numeric values and type converting string to int
        items['rounds'] = int(re.sub('[^0-9]','', rounds.split(" Round:\n        </i>\n ")[-1]))

        # Extracts the time the bout ended.
        items['time'] = response.xpath("//p[1]//i[3]").extract()[0].split()[-2]
        date_time = datetime.strptime(items['time'], '%M:%S').time()
        items['time_seconds'] = date_time.minute * 60 + date_time.second

        # Obtains the all important stats table.
        fight_stats_table = response.xpath("//p[@class='b-fight-details__table-text']").extract()

        # Extracts the total fight stats
        for ind,stat in enumerate(fight_stats_table, start=0):
            # Set fighter number.
            if ind % 2 == 0:
                fighter_num = 'f1'
            else:
                fighter_num = 'f2'

            # Extracts the fighter detail urls.
            if ind == 0:
                items['fighter_1_detail_url'] = stat.split('href')[1].split('"')[1]
            elif ind == 1:
                items['fighter_2_detail_url'] = stat.split('href')[1].split('"')[1]

            # Set statistic type (total or round by round)
            time_type_ind = int(ind / 20)
            if time_type_ind == 0:
                time_type = 'tot'
            else:
                time_type = f'r{time_type_ind}'

            # Set a base index so that it runs iteratively for each round.
            base_ind = ind % 20
            if 2 <= base_ind <= 3:
                items[f'{fighter_num}_{time_type}_kd'] = int(re.sub('[^0-9]', '', stat))
            elif 4 <= base_ind <= 5:
                items[f'{fighter_num}_{time_type}_ss_l'], items[f'{fighter_num}_tot_ss_a'] = self.extract_number_of(stat)
            elif 8 <= base_ind <= 9:
                items[f'{fighter_num}_{time_type}_s_l'], items[f'{fighter_num}_tot_s_a'] = self.extract_number_of(stat)
            elif 10 <= base_ind <= 11:
                items[f'{fighter_num}_{time_type}_td_l'], items[f'{fighter_num}_tot_td_a'] = self.extract_number_of(stat)
            elif 14 <= base_ind <= 15:
                items[f'{fighter_num}_{time_type}_sub_a'] = int(re.sub('[^0-9]', '', stat))
            elif 16 <= base_ind <= 17:
                items[f'{fighter_num}_{time_type}_pass'] = int(re.sub('[^0-9]', '', stat))
            elif 18 <= base_ind <= 19:
                items[f'{fighter_num}_{time_type}_rev'] = int(re.sub('[^0-9]', '', stat))

            if(ind >= 20 * (items['rounds'] + 1)):
                break


        yield items
