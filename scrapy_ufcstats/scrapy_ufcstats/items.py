# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyUfcstatsItem(scrapy.Item):
    # define the fields for your item here like:
    division = scrapy.Field()
    fighter_1 = scrapy.Field()
    fighter_1_nn = scrapy.Field()
    fighter_1_detail_url = scrapy.Field()
    fighter_2 = scrapy.Field()
    fighter_2_nn = scrapy.Field()
    fighter_2_detail_url = scrapy.Field()
    winner = scrapy.Field()
    win_method = scrapy.Field()
    win_method_details = scrapy.Field()
    referee = scrapy.Field()
    date = scrapy.Field()
    rounds = scrapy.Field()
    time = scrapy.Field()
    time_seconds = scrapy.Field()

    # Fighter 1 totals.
    f1_tot_kd = scrapy.Field()
    f1_tot_ss_l = scrapy.Field()
    f1_tot_ss_a = scrapy.Field()
    f1_tot_s_l = scrapy.Field()
    f1_tot_s_a = scrapy.Field()
    f1_tot_td_l = scrapy.Field()
    f1_tot_td_a = scrapy.Field()
    f1_tot_sub_a = scrapy.Field()
    f1_tot_pass = scrapy.Field()
    f1_tot_rev = scrapy.Field()
    f1_r1_kd = scrapy.Field()
    f1_r1_ss_l = scrapy.Field()
    f1_r1_ss_a = scrapy.Field()
    f1_r1_s_l = scrapy.Field()
    f1_r1_s_a = scrapy.Field()
    f1_r1_td_l = scrapy.Field()
    f1_r1_td_a = scrapy.Field()
    f1_r1_sub_a = scrapy.Field()
    f1_r1_pass = scrapy.Field()
    f1_r1_rev = scrapy.Field()
    f1_r2_kd = scrapy.Field()
    f1_r2_ss_l = scrapy.Field()
    f1_r2_ss_a = scrapy.Field()
    f1_r2_s_l = scrapy.Field()
    f1_r2_s_a = scrapy.Field()
    f1_r2_td_l = scrapy.Field()
    f1_r2_td_a = scrapy.Field()
    f1_r2_sub_a = scrapy.Field()
    f1_r2_pass = scrapy.Field()
    f1_r2_rev = scrapy.Field()
    f1_r3_kd = scrapy.Field()
    f1_r3_ss_l = scrapy.Field()
    f1_r3_ss_a = scrapy.Field()
    f1_r3_s_l = scrapy.Field()
    f1_r3_s_a = scrapy.Field()
    f1_r3_td_l = scrapy.Field()
    f1_r3_td_a = scrapy.Field()
    f1_r3_sub_a = scrapy.Field()
    f1_r3_pass = scrapy.Field()
    f1_r3_rev = scrapy.Field()
    f1_r4_kd = scrapy.Field()
    f1_r4_ss_l = scrapy.Field()
    f1_r4_ss_a = scrapy.Field()
    f1_r4_s_l = scrapy.Field()
    f1_r4_s_a = scrapy.Field()
    f1_r4_td_l = scrapy.Field()
    f1_r4_td_a = scrapy.Field()
    f1_r4_sub_a = scrapy.Field()
    f1_r4_pass = scrapy.Field()
    f1_r4_rev = scrapy.Field()
    f1_r5_kd = scrapy.Field()
    f1_r5_ss_l = scrapy.Field()
    f1_r5_ss_a = scrapy.Field()
    f1_r5_s_l = scrapy.Field()
    f1_r5_s_a = scrapy.Field()
    f1_r5_td_l = scrapy.Field()
    f1_r5_td_a = scrapy.Field()
    f1_r5_sub_a = scrapy.Field()
    f1_r5_pass = scrapy.Field()
    f1_r5_rev = scrapy.Field()

    # Fighter 1 significant strike origins and destinations
    f1_tot_ss_head_l = scrapy.Field()
    f1_tot_ss_head_a = scrapy.Field()
    f1_tot_ss_body_l = scrapy.Field()
    f1_tot_ss_body_a = scrapy.Field()
    f1_tot_ss_leg_l = scrapy.Field()
    f1_tot_ss_leg_a = scrapy.Field()
    f1_tot_distance_l = scrapy.Field()
    f1_tot_distance_a = scrapy.Field()
    f1_tot_clinch_l = scrapy.Field()
    f1_tot_clinch_a = scrapy.Field()
    f1_tot_ground_l = scrapy.Field()
    f1_tot_ground_a = scrapy.Field()
    f1_r1_ss_head_l = scrapy.Field()
    f1_r1_ss_head_a = scrapy.Field()
    f1_r1_ss_body_l = scrapy.Field()
    f1_r1_ss_body_a = scrapy.Field()
    f1_r1_ss_leg_l = scrapy.Field()
    f1_r1_ss_leg_a = scrapy.Field()
    f1_r1_distance_l = scrapy.Field()
    f1_r1_distance_a = scrapy.Field()
    f1_r1_clinch_l = scrapy.Field()
    f1_r1_clinch_a = scrapy.Field()
    f1_r1_ground_l = scrapy.Field()
    f1_r1_ground_a = scrapy.Field()
    f1_r2_ss_head_l = scrapy.Field()
    f1_r2_ss_head_a = scrapy.Field()
    f1_r2_ss_body_l = scrapy.Field()
    f1_r2_ss_body_a = scrapy.Field()
    f1_r2_ss_leg_l = scrapy.Field()
    f1_r2_ss_leg_a = scrapy.Field()
    f1_r2_distance_l = scrapy.Field()
    f1_r2_distance_a = scrapy.Field()
    f1_r2_clinch_l = scrapy.Field()
    f1_r2_clinch_a = scrapy.Field()
    f1_r2_ground_l = scrapy.Field()
    f1_r2_ground_a = scrapy.Field()
    f1_r3_ss_head_l = scrapy.Field()
    f1_r3_ss_head_a = scrapy.Field()
    f1_r3_ss_body_l = scrapy.Field()
    f1_r3_ss_body_a = scrapy.Field()
    f1_r3_ss_leg_l = scrapy.Field()
    f1_r3_ss_leg_a = scrapy.Field()
    f1_r3_distance_l = scrapy.Field()
    f1_r3_distance_a = scrapy.Field()
    f1_r3_clinch_l = scrapy.Field()
    f1_r3_clinch_a = scrapy.Field()
    f1_r3_ground_l = scrapy.Field()
    f1_r3_ground_a = scrapy.Field()
    f1_r4_ss_head_l = scrapy.Field()
    f1_r4_ss_head_a = scrapy.Field()
    f1_r4_ss_body_l = scrapy.Field()
    f1_r4_ss_body_a = scrapy.Field()
    f1_r4_ss_leg_l = scrapy.Field()
    f1_r4_ss_leg_a = scrapy.Field()
    f1_r4_distance_l = scrapy.Field()
    f1_r4_distance_a = scrapy.Field()
    f1_r4_clinch_l = scrapy.Field()
    f1_r4_clinch_a = scrapy.Field()
    f1_r4_ground_l = scrapy.Field()
    f1_r4_ground_a = scrapy.Field()
    f1_r5_ss_head_l = scrapy.Field()
    f1_r5_ss_head_a = scrapy.Field()
    f1_r5_ss_body_l = scrapy.Field()
    f1_r5_ss_body_a = scrapy.Field()
    f1_r5_ss_leg_l = scrapy.Field()
    f1_r5_ss_leg_a = scrapy.Field()
    f1_r5_distance_l = scrapy.Field()
    f1_r5_distance_a = scrapy.Field()
    f1_r5_clinch_l = scrapy.Field()
    f1_r5_clinch_a = scrapy.Field()
    f1_r5_ground_l = scrapy.Field()
    f1_r5_ground_a = scrapy.Field()


    # Fighter 2 totals.
    f2_tot_kd = scrapy.Field()
    f2_tot_ss_l = scrapy.Field()
    f2_tot_ss_a = scrapy.Field()
    f2_tot_s_l = scrapy.Field()
    f2_tot_s_a = scrapy.Field()
    f2_tot_td_l = scrapy.Field()
    f2_tot_td_a = scrapy.Field()
    f2_tot_sub_a = scrapy.Field()
    f2_tot_pass = scrapy.Field()
    f2_tot_rev = scrapy.Field()
    f2_tot_distance_l = scrapy.Field()
    f2_tot_distance_a = scrapy.Field()
    f2_tot_clinch_l = scrapy.Field()
    f2_tot_clinch_a = scrapy.Field()
    f2_tot_ground_l = scrapy.Field()
    f2_tot_ground_a = scrapy.Field()
    f2_r1_kd = scrapy.Field()
    f2_r1_ss_l = scrapy.Field()
    f2_r1_ss_a = scrapy.Field()
    f2_r1_s_l = scrapy.Field()
    f2_r1_s_a = scrapy.Field()
    f2_r1_td_l = scrapy.Field()
    f2_r1_td_a = scrapy.Field()
    f2_r1_sub_a = scrapy.Field()
    f2_r1_pass = scrapy.Field()
    f2_r1_rev = scrapy.Field()
    f2_r1_distance_l = scrapy.Field()
    f2_r1_distance_a = scrapy.Field()
    f2_r1_clinch_l = scrapy.Field()
    f2_r1_clinch_a = scrapy.Field()
    f2_r1_ground_l = scrapy.Field()
    f2_r1_ground_a = scrapy.Field()
    f2_r2_kd = scrapy.Field()
    f2_r2_ss_l = scrapy.Field()
    f2_r2_ss_a = scrapy.Field()
    f2_r2_s_l = scrapy.Field()
    f2_r2_s_a = scrapy.Field()
    f2_r2_td_l = scrapy.Field()
    f2_r2_td_a = scrapy.Field()
    f2_r2_sub_a = scrapy.Field()
    f2_r2_pass = scrapy.Field()
    f2_r2_rev = scrapy.Field()
    f2_r2_distance_l = scrapy.Field()
    f2_r2_distance_a = scrapy.Field()
    f2_r2_clinch_l = scrapy.Field()
    f2_r2_clinch_a = scrapy.Field()
    f2_r2_ground_l = scrapy.Field()
    f2_r2_ground_a = scrapy.Field()
    f2_r3_kd = scrapy.Field()
    f2_r3_ss_l = scrapy.Field()
    f2_r3_ss_a = scrapy.Field()
    f2_r3_s_l = scrapy.Field()
    f2_r3_s_a = scrapy.Field()
    f2_r3_td_l = scrapy.Field()
    f2_r3_td_a = scrapy.Field()
    f2_r3_sub_a = scrapy.Field()
    f2_r3_pass = scrapy.Field()
    f2_r3_rev = scrapy.Field()
    f2_r3_distance_l = scrapy.Field()
    f2_r3_distance_a = scrapy.Field()
    f2_r3_clinch_l = scrapy.Field()
    f2_r3_clinch_a = scrapy.Field()
    f2_r3_ground_l = scrapy.Field()
    f2_r3_ground_a = scrapy.Field()
    f2_r4_kd = scrapy.Field()
    f2_r4_ss_l = scrapy.Field()
    f2_r4_ss_a = scrapy.Field()
    f2_r4_s_l = scrapy.Field()
    f2_r4_s_a = scrapy.Field()
    f2_r4_td_l = scrapy.Field()
    f2_r4_td_a = scrapy.Field()
    f2_r4_sub_a = scrapy.Field()
    f2_r4_pass = scrapy.Field()
    f2_r4_rev = scrapy.Field()
    f2_r4_distance_l = scrapy.Field()
    f2_r4_distance_a = scrapy.Field()
    f2_r4_clinch_l = scrapy.Field()
    f2_r4_clinch_a = scrapy.Field()
    f2_r4_ground_l = scrapy.Field()
    f2_r4_ground_a = scrapy.Field()
    f2_r5_kd = scrapy.Field()
    f2_r5_ss_l = scrapy.Field()
    f2_r5_ss_a = scrapy.Field()
    f2_r5_s_l = scrapy.Field()
    f2_r5_s_a = scrapy.Field()
    f2_r5_td_l = scrapy.Field()
    f2_r5_td_a = scrapy.Field()
    f2_r5_sub_a = scrapy.Field()
    f2_r5_pass = scrapy.Field()
    f2_r5_rev = scrapy.Field()
    f2_r5_distance_l = scrapy.Field()
    f2_r5_distance_a = scrapy.Field()
    f2_r5_clinch_l = scrapy.Field()
    f2_r5_clinch_a = scrapy.Field()
    f2_r5_ground_l = scrapy.Field()
    f2_r5_ground_a = scrapy.Field()

    # Fighter 1 significant strike origins and destinations
    f2_tot_ss_head_l = scrapy.Field()
    f2_tot_ss_head_a = scrapy.Field()
    f2_tot_ss_body_l = scrapy.Field()
    f2_tot_ss_body_a = scrapy.Field()
    f2_tot_ss_leg_l = scrapy.Field()
    f2_tot_ss_leg_a = scrapy.Field()
    f2_r1_ss_head_l = scrapy.Field()
    f2_r1_ss_head_a = scrapy.Field()
    f2_r1_ss_body_l = scrapy.Field()
    f2_r1_ss_body_a = scrapy.Field()
    f2_r1_ss_leg_l = scrapy.Field()
    f2_r1_ss_leg_a = scrapy.Field()
    f2_r2_ss_head_l = scrapy.Field()
    f2_r2_ss_head_a = scrapy.Field()
    f2_r2_ss_body_l = scrapy.Field()
    f2_r2_ss_body_a = scrapy.Field()
    f2_r2_ss_leg_l = scrapy.Field()
    f2_r2_ss_leg_a = scrapy.Field()
    f2_r3_ss_head_l = scrapy.Field()
    f2_r3_ss_head_a = scrapy.Field()
    f2_r3_ss_body_l = scrapy.Field()
    f2_r3_ss_body_a = scrapy.Field()
    f2_r3_ss_leg_l = scrapy.Field()
    f2_r3_ss_leg_a = scrapy.Field()
    f2_r4_ss_head_l = scrapy.Field()
    f2_r4_ss_head_a = scrapy.Field()
    f2_r4_ss_body_l = scrapy.Field()
    f2_r4_ss_body_a = scrapy.Field()
    f2_r4_ss_leg_l = scrapy.Field()
    f2_r4_ss_leg_a = scrapy.Field()
    f2_r5_ss_head_l = scrapy.Field()
    f2_r5_ss_head_a = scrapy.Field()
    f2_r5_ss_body_l = scrapy.Field()
    f2_r5_ss_body_a = scrapy.Field()
    f2_r5_ss_leg_l = scrapy.Field()
    f2_r5_ss_leg_a = scrapy.Field()

    location = scrapy.Field()
    attendance = scrapy.Field()
    url = scrapy.Field()
