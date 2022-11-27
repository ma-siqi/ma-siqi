#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:21:57 2022

@author: maguo
"""


from apiclient.discovery import build
import json

DEVELOPER_KEY = 'AIzaSyDG2XqteQKyQ-BcYT3l3sap7PQqNLG6oks'
#DEVELOPER_KEY = 'AIzaSyCefJGUrVDdC-QTFlaTzMS7s6WE63i4ODE'
JSON_PATH = 'meta_filtered.json'
URL_PATH = 'filtered_url_list.txt'
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

def getid(url):
    ytid = url.find('=')+1
    return url[ytid:]

def metadata(ytid):
    result = youtube.videos().list(id=ytid, part="id, snippet,contentDetails,liveStreamingDetails,player,statistics,status, topicDetails").execute()
    data = {}
    if result['pageInfo']['totalResults']!=1:
        print("no result/not unique ID. ")
        data[ytid] = {}
        return data
    else:
        stats = result['items']
        item = stats[0]
        #attributes in snippet (publishedAt, channelId, channelTitle, categoryId, videoTitle, description)
        publishedAt = item['snippet']['publishedAt']
        channelId = item['snippet']['channelId']   
        channelTitle = item['snippet']['channelTitle']
        categoryId = item['snippet']['categoryId']
        title = item['snippet']['title']
        description = item['snippet']['description']
        channelPublishedat = ""
        channelDescription = ""
        channelSubscriberCount = ""
        channelViewCount = ""
        channelCommentCount = ""
        channelVideoCount = ""
        channel_details=youtube.channels().list(id=channelId,part="snippet,statistics").execute()
        for channel in channel_details.get("items",[]):
            try:
                channelPublishedat = channel['snippet'].get('publishedAt', '')
                channelDescription = channel['snippet'].get('description', '')
                channelSubscriberCount = channel['statistics'].get('subscriberCount',0)
                channelViewCount = channel['statistics'].get('viewCount',0)
                channelCommentCount = channel['statistics'].get("commentCount",0)
                channelVideoCount =channel['statistics'].get('videoCount',0)
            except KeyError as e:
                print("An KeyError error %d occurred:\n%s" % (e.resp.status, e.content))
        #attributes in contentDetails(duration, dimension,definition,caption,licensed)
        contentDuration = item['contentDetails']['duration']
        contentDimension = item['contentDetails']['dimension']
        contentDefinition = item['contentDetails']['definition']
        contentCaption = item['contentDetails']['caption']
        contentLicensed = item['contentDetails']['licensedContent']
        contentRating = item['contentDetails'].get('contentRating',{})
        #attributes in status(uploadStatus,privacyStatus, license, embeddable,publicStatsViewable)
        uploadStatus = item['status']['uploadStatus']
        privacyStatus = item['status']['privacyStatus']
        videolicense =item['status']['license']
        embeddable = item['status']['embeddable']
        publicStatsViewable = item['status']['publicStatsViewable']
        #attributes in statistics(viewCount, likeCount, dislikeCount,favoriteCount,commentCount)
        viewCount = item['statistics'].get('viewCount',0)
        likeCount = item['statistics'].get('likeCount',0)
        dislikeCount = item['statistics'].get('dislikeCount',0)
        favoriteCount = item['statistics'].get('favoriteCount',0)
        commentCount = item['statistics'].get('commentCount',0)
        #attributes from topicDetails (topicIds, relevantTopicIds)
        topicIds = item.get('topicDetails',{}).get('topicIds','')
        relevantTopicIds = item.get('topicDetails',{}).get('relevantTopicIds','')
            
        data[ytid] = {
            'Title': title,
            'Description': description,
            'ChannelDetails':{
                    'ChannelId': channelId,
                    'ChannelTitle': channelTitle,
                    'ChannelPublishedat': channelPublishedat,
                    'ChannelDescription': channelDescription,
                    'ChannelSubscriberCount': channelSubscriberCount,
                    'ChannelViewCount': channelViewCount,
                    'ChannelCommenCount': channelCommentCount,
                    'ChannelVideoCount': channelVideoCount},
            'PublishedAt': publishedAt,
            'CategoryId': categoryId,
            'Duration': contentDuration,
            'Dimension': contentDimension,
            'Definition': contentDefinition,
            'Caption': contentCaption,
            'Licensed': contentLicensed,
            'Rating': contentRating,
            'UploadStatus': uploadStatus,
            'Privacy': privacyStatus,
            'VideoLicense': videolicense,
            'Embeddable': embeddable,
            'PublicStatsViewable': publicStatsViewable,
            'Views': viewCount,
            'Likes': likeCount,
            'Dislikes': dislikeCount,
            'Favorites': favoriteCount,
            'CommentCount': commentCount,
            'TopicsIds': topicIds,
            'RelevantTopicIds': relevantTopicIds 
            }
    print("fetching data for" + ytid)
    return data
      
with open(JSON_PATH,'a') as fout:
    with open(URL_PATH, 'r') as file:
        for lines in file:
            #print(ytid)
            fout.write(json.dumps(metadata(lines.rstrip()), indent = 2))


#testid = getid("https://www.youtube.com/watch?v=IxtMp__sH4w")
#test = metadata(testid)

#testid = '5rC0qpLGciU'

#result = youtube.videos().list(id=testid, part="id, snippet,contentDetails,liveStreamingDetails,player,statistics,status, topicDetails").execute()

#stats =  result['items'][0]
