#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:01:14 2022

@author: Siqi Ma
"""

import requests
import json


def import_video_data(URL):
    print('Fetching Video page source using URL ' + URL)
    page_source = requests.get(URL)
    page_source = page_source.text
    start_index = page_source.find('ytInitialData')
    tmp = page_source[ start_index+17:]
    end_index = tmp.find('}};')
    tmp = '{' + tmp[:end_index] + '}}'
    return tmp

def parse_json(json_data):
    json_dict = json.loads(json_data)
    return json_dict

    
def find_desc(url):
    session = requests.Session()
    response = session.get(url)

    html = response.text
    description = find_value(html, '<meta name="description" content=', '">')[1:]
    return description


def find_dislike(url):
    r = requests.get(url, headers={'User-Agent': ''})
    dl = r.text[:r.text.find(' dislikes"')]
    dislike = dl[dl.rfind('"') + 1:]
    return dislike
    
def find_value(html, key, separator):
    pos_begin = html.find(key) + len(key)-1
    pos_end = html.find(separator, pos_begin) + len(separator)-1
    return html[pos_begin: pos_end]


def meta(url):
    yt_json = parse_json(import_video_data(url))
    video_id = yt_json['currentVideoEndpoint']['watchEndpoint']['videoId']
    public = True
    availiable = True
    try:
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents']
    except:
        public = False
    
    if public:
        try:
            content = yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
            
        except: 
            try:
                content = yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoPrimaryInfoRenderer']
            except:
                availiable = False
    if public and availiable:
        title = content['title']['runs'][0]['text']
        try:
            views = content['viewCount']['videoViewCountRenderer']['viewCount']['simpleText']
        except:
            views = None
        try:
            likes = content['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
        except:
            likes = None
    else:
        title = None
        views= None
        likes = None
    #dislikes = yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][1]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
    
    description = find_desc(url)
    #dislikes = find_dislike(url)
    data = {}
    if public:
        data[video_id] = {
                'title': title,
                'video_id': video_id,
                'url': url,
                'views': views,
                'likes': likes,
                #'dislikes': dislikes,
                'description': description,
                'type': 'public',
                }
    else:
        data[url] = {'type':'Private'}
        
    return data

def meta_list(path, JSON_PATH):
    with open(JSON_PATH,'a') as fout:
        with open(path, 'r') as file:
            for lines in file:
                fout.write(json.dumps(meta(lines), indent = 2))

meta_list('urlleft.txt', 'meta1.json')
