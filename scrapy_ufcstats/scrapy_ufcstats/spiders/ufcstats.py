# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from ..items import ScrapyUfcstatsItem
from datetime import datetime
import pendulum
import re


class UfcstatsSpider(Spider):
    name = 'fights'

    def start_requests(self):
        urls = [
            'http://www.ufcstats.com/statistics/events/completed?page=all'
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        # Finds all event_urls within the start page.
        for event_url in response.css('.b-link_style_black::attr(href)').getall():
            yield Request(event_url, callback=self.parse_event)


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
        attendance = int(attendance.replace(',',''))

        # Fetches all fight urls from each event.
        for fight_url in response.css('a.b-flag_style_green::attr(href)').getall():
            yield Request(fight_url,
                          callback=self.parse_fight,
                          meta={'date': date, 'location': location, 'attendance': attendance})


    def parse_fight(self, response):
        # Appends meta data from previous parsing layer.
        date = response.meta['date']
        location = response.meta['location']
        attendance = response.meta['attendance']

        # Appends data from each fight.
        items = ScrapyUfcstatsItem()
        print(response.url)

        # Extracts fighter name.
        fighters = response.xpath("//h3[@class='b-fight-details__person-name']//a/text()").extract()
        if len(fighters) == 0:
            fighters = response.xpath("//h3[@class='b-fight-details__person-name']/span/text()").extract()

        # Extracts fighter nicknames.
        nicknames = response.xpath("//p[@class='b-fight-details__person-title']/text()").extract()

        # Data wrangles names.
        fighter_1 = fighters[0].strip()
        fighter_1_nn = nicknames[0].strip()
        fighter_2 = fighters[1].strip()
        fighter_2_nn = nicknames[1].strip()

        # Appends winner.
        fighter_1_outcome = response.xpath("//body[@class='b-page']/section[@class='b-statistics__section_details']"
                                           "/div[@class='l-page__container']/div[@class='b-fight-details']"
                                           "/div[@class='b-fight-details__persons clearfix']"
                                           "/div[1]/i/text()").extract()
        fighter_1_outcome = fighter_1_outcome[0].strip()
        if fighter_1_outcome == "W":
            winner = fighter_1
        else:
            winner = fighter_2

        # Appends number of rounds fought.
        rounds = response.xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[2]/p[1]/i[2]").get()
        # Data wrangles rounds by getting rid of all non numeric values and type converting string to int
        rounds = int(re.sub('[^0-9]','', rounds.split(" Round:\n        </i>\n ")[-1]))

        # Appends round by round stats
        fight_stats_table = response.xpath("//p[@class='b-fight-details__table-text']").extract()
        for ind,stat in enumerate(fight_stats_table, start=0):
            if ind == 2:
                f1_r1_kd = int(re.sub('[^0-9]', '', stat))
            elif ind == 3:
                f2_r1_kd = int(re.sub('[^0-9]', '', stat))
            elif ind == 4:
                f1_r1_ss_l = int(re.sub('[^0-9]', '', stat.split('of')[0]))
                f1_r1_ss_a = int(re.sub('[^0-9]', '', stat.split('of')[1]))
            elif ind == 5:
                f2_r1_ss_l = int(re.sub('[^0-9]', '', stat.split('of')[0]))
                f2_r1_ss_a = int(re.sub('[^0-9]', '', stat.split('of')[1]))
            elif ind == 8:
                f1_r1_s_l = int(re.sub('[^0-9]', '', stat.split('of')[0]))
                f1_r1_s_a = int(re.sub('[^0-9]', '', stat.split('of')[1]))
            elif ind == 9:
                f2_r1_s_l = int(re.sub('[^0-9]', '', stat.split('of')[0]))
                f2_r1_s_a = int(re.sub('[^0-9]', '', stat.split('of')[1]))

        # Itemizes the extracted data
        items['fighter_1'] = fighter_1
        items['fighter_1_nn'] = fighter_1_nn
        items['fighter_2'] = fighter_2
        items['fighter_2_nn'] = fighter_2_nn
        items['winner'] = winner
        items['rounds'] = rounds

        # Itemizes the round by round data.
        items['f1_r1_kd'] = f1_r1_kd
        items['f2_r1_kd'] = f2_r1_kd
        items['f1_r1_ss_l'] = f1_r1_ss_l
        items['f1_r1_ss_a'] = f1_r1_ss_a
        items['f2_r1_ss_l'] = f2_r1_ss_l
        items['f2_r1_ss_a'] = f2_r1_ss_a
        items['f2_r1_ss_a'] = f2_r1_ss_a
        items['f1_r1_s_l'] = f1_r1_s_l
        items['f1_r1_s_a'] = f1_r1_s_a
        items['f2_r1_s_l'] = f2_r1_s_l
        items['f2_r1_s_a'] = f2_r1_s_a


        # Itemizes general even information
        items['date'] = date
        items['location'] = location
        items['attendance'] = attendance

        yield items
