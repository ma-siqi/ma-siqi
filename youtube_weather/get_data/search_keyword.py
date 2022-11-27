#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:53:11 2022

@author: Siqi Ma
"""

from selenium import webdriver
import json


YOUTUBE_SEARCH = 'https://www.youtube.com/results?search_query={word_input}'


def get_video_results(keyword):
    driver = webdriver.Chrome(executable_path='/Users/maguo/Desktop/scrapers_yt/wf/chromedriver')
    driver.get(YOUTUBE_SEARCH.format(word_input=keyword))

    youtube_data = {}

    # scrolling to the end of the page
    # https://stackoverflow.com/a/57076690/15164646
    while True:
        # end_result = "No more results" string at the bottom of the page
        # this will be used to break out of the while loop
        end_result = driver.find_element_by_css_selector('#message').is_displayed()
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        # time.sleep(1) # could be removed
        print(end_result)

        # once element is located, break out of the loop
        if end_result == True:
            break

    print('Extracting results. It might take a while...')

    for result in driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element_by_css_selector('.long-byline').text
        channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
        views = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[0]

        try:
            time_published = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[1]
        except:
            time_published = None

        try:
            snippet = result.find_element_by_css_selector('.metadata-snippet-container').text
        except:
            snippet = None

        try:
            if result.find_element_by_css_selector('#channel-name .ytd-badge-supported-renderer') is not None:
                verified_badge = True
            else:
                verified_badge = False
        except:
            verified_badge = None

        try:
            extensions = result.find_element_by_css_selector('#badges .ytd-badge-supported-renderer').text
        except:
            extensions = None
        print(verified_badge)
        
        ytid = link[-11:-2]

        youtube_data[ytid]= {
            'title': title,
            'link': link,
            'channel': {'channel_name': channel_name, 'channel_link': channel_link},
            'views': views,
            'time_published': time_published,
            'snippet': snippet,
            'verified_badge': verified_badge,
            'extensions': extensions,
            'search_keyword': keyword,
        }

    driver.quit()
    return youtube_data
    
    
def get_idlist(path, JSON_PATH):
    with open(JSON_PATH,'a') as fout:
        with open(path, 'r') as file:
            for line in file:
                fout.write(json.dumps(get_video_results(line), indent = 2))


get_idlist('drought_heat_flood_hurricanes.txt', 'search_result.json')              


