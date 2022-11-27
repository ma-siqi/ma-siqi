#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:23:31 2022

@author: maguo
"""

import json

#DEVELOPER_KEY = 'AIzaSyDG2XqteQKyQ-BcYT3l3sap7PQqNLG6oks'
#DEVELOPER_KEY = 'AIzaSyCNXSmu0UEtIH_fu7rmwv0riCJVNV_Xag'
DEVELOPER_KEY = 'AIzaSyCefJGUrVDdC-QTFlaTzMS7s6WE63i4ODE'

from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)



def scrape_comments_with_replies(id_code):
    box = [['Name', 'Comment', 'Time', 'Likes', 'Reply Count']]
    df = {}
    try:
        data = youtube.commentThreads().list(part='snippet', videoId=id_code, maxResults='100', textFormat="plainText").execute()
    except:
        return df
    
    for i in data["items"]:
        name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
        likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
        replies = i["snippet"]['totalReplyCount']
            
        box.append([name, comment, published_at, likes, replies])
            
        totalReplyCount = i["snippet"]['totalReplyCount']
            
        if totalReplyCount > 0:
                
            parent = i["snippet"]['topLevelComment']["id"]
                
            data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                            textFormat="plainText").execute()
                
            for i in data2["items"]:
                name = i["snippet"]["authorDisplayName"]
                comment = i["snippet"]["textDisplay"]
                published_at = i["snippet"]['publishedAt']
                likes = i["snippet"]['likeCount']
                replies = ""

                box.append([name, comment, published_at, likes, replies])

    while ("nextPageToken" in data):
            
        data = youtube.commentThreads().list(part='snippet', videoId=id_code, pageToken=data["nextPageToken"],
                                             maxResults='100', textFormat="plainText").execute()
                                             
        for i in data["items"]:
            name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
            published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
            likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
            replies = i["snippet"]['totalReplyCount']

            box.append([name, comment, published_at, likes, replies])

            totalReplyCount = i["snippet"]['totalReplyCount']

            if totalReplyCount > 0:
                    
                parent = i["snippet"]['topLevelComment']["id"]

                data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                                    textFormat="plainText").execute()

                for i in data2["items"]:
                    name = i["snippet"]["authorDisplayName"]
                    comment = i["snippet"]["textDisplay"]
                    published_at = i["snippet"]['publishedAt']
                    likes = i["snippet"]['likeCount']
                    replies = ''

                    box.append([name, comment, published_at, likes, replies])

    df[id_code] = {
            'Name': [i[0] for i in box], 
            'Comment': [i[1] for i in box], 
            'Time': [i[2] for i in box],
            'Likes': [i[3] for i in box], 
            'Reply Count': [i[4] for i in box]}
        
    return df
    
    
with open('comment3.json','a') as fout:
    with open('rerun.txt', 'r') as file:
        for lines in file:
            print('scraping comment for video {0}'.format(lines))
            data = {}
            data[lines.rstrip()] = scrape_comments_with_replies(lines.rstrip())
            fout.write('{0}\n'.format(json.dumps(data, indent = 2)))
    

