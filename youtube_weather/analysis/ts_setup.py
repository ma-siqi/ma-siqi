#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:37:56 2022

@author: maguo
"""


import pandas as pd
from datetime import date
import math

data = pd.read_json('analysis_meta.json').T

orig = pd.read_csv('did_setup.csv')

diaster_data = pd.read_csv('Diasters.csv')

weather_key = pd.read_csv('key_weather.csv')

weather_dic = {}

#Have a dictionary of key to weather
for i in range(weather_key.shape[0]):
    weather_dic[weather_key['search-key'][i]] = weather_key['Type'][i]


#Label each diaster correctly

weather_code = []
missed = []
for video in list(data.index):
    print(video)
    if video in list(orig['X']):
        index = list(orig['X']).index(video)
        weather = orig["W"][index]
        print(weather)
        if weather == 1:
            print('fire')
            weather_code.append("FI")
        elif weather == 0:
            print('hurricane')
            weather_code.append('HU')
    else:
        print('new video')
        index = list(data.index).index(video)
        key = data['search_key'][index].rstrip()
        try:
            weather_code.append(weather_dic[key])
        except:
            weather_code.append('FI')
    
data['W'] = weather_code  

#Import topic matrix

hold_df = pd.DataFrame()

matrix = pd.read_json('topic_matrix.json')
    
    
#Calculate indicator for each week
time_weather_dict = dict()

weather_type = ['HW', 'FI', 'DR', 'HU', 'FL']
for i in ['HW', 'FI', 'DR', 'HU', 'FL', 'NONE']:
    time_weather_dict[i] = [0]*835

time = pd.read_csv('diaster_nbw_1y.csv')

for i in range(835):
    for weather in weather_type:
        temp = time[time['code'] == weather]
        temp.index = range(temp.shape[0])
        for j in range(temp.shape[0]):
            if i > temp.at[j, 'from'] and i < temp.at[j, 'to']:
                time_weather_dict[weather][i] = 1 

#Calculate the time series for each video
base = abs(date(1970,1,1) - date(2006,1,1)).days


merge_list = []
weather_list = list(data['W'])
year = []
id_list = matrix.columns.values.tolist()
for j in range(835):
    year.append(j//52) 

for k in range(matrix.shape[1]):
    check = 0
    temp_df = pd.DataFrame()
    temp_df['year'] = year
    temp_df['time'] = range(835)
    temp_df['video_id'] = [id_list[k]] * 835
    temp_df['count'] = matrix.at[0, id_list[k]]
    temp_df['L1'] = matrix.at[1, id_list[k]]
    temp_df['L2'] = matrix.at[2, id_list[k]]
    temp_df['L3'] = matrix.at[3, id_list[k]]
    temp_df['L4'] = matrix.at[4, id_list[k]]
    temp_df['L5'] = matrix.at[5, id_list[k]]
    temp_df['L6'] = matrix.at[6, id_list[k]]
    temp_df['L7'] = matrix.at[7, id_list[k]]
    temp_df['L8'] = matrix.at[8, id_list[k]]
    temp_df['L9'] = matrix.at[9, id_list[k]]
    temp_df['L10'] = matrix.at[10, id_list[k]]
    temp_df['L11'] = matrix.at[11, id_list[k]]
    temp_df['L12'] = matrix.at[12, id_list[k]]
    temp_df['L13'] = matrix.at[13, id_list[k]]
    temp_df['L14'] = matrix.at[14, id_list[k]]
    temp_df['L15'] = matrix.at[15, id_list[k]]
    temp_df['L16'] = matrix.at[16, id_list[k]]
    temp_df['L17'] = matrix.at[17, id_list[k]]
    temp_df['L18'] = matrix.at[18, id_list[k]]
    temp_df['L19'] = matrix.at[19, id_list[k]]
    temp_df['L20'] = matrix.at[20, id_list[k]]
    temp_df['L21'] = matrix.at[21, id_list[k]]
    temp_df['L22'] = matrix.at[22, id_list[k]]
    temp_df['L23'] = matrix.at[23, id_list[k]]
    temp_df['L24'] = matrix.at[24, id_list[k]]
    temp_df['L25'] = matrix.at[25, id_list[k]]
    temp_df['L26'] = matrix.at[26, id_list[k]]
    temp_df['L27'] = matrix.at[27, id_list[k]]
    temp_df['L28'] = matrix.at[28, id_list[k]]
    temp_df['L29'] = matrix.at[29, id_list[k]]
    temp_df['L30'] = matrix.at[30, id_list[k]]
    temp_df['L31'] = matrix.at[31, id_list[k]]
    temp_df['L32'] = matrix.at[32, id_list[k]]
    temp_df['L33'] = matrix.at[33, id_list[k]]
    temp_df['L34'] = matrix.at[34, id_list[k]]
    temp_df['L35'] = matrix.at[35, id_list[k]]
    temp_df['L36'] = matrix.at[36, id_list[k]]
    temp_df['L37'] = matrix.at[37, id_list[k]]
    temp_df['L38'] = matrix.at[38, id_list[k]]
    temp_df['L39'] = matrix.at[39, id_list[k]]
    temp_df['L40'] = matrix.at[40, id_list[k]]
    temp_df['L41'] = matrix.at[41, id_list[k]]
    temp_df['L42'] = matrix.at[42, id_list[k]]
    temp_df['L43'] = matrix.at[43, id_list[k]]
    temp_df['L44'] = matrix.at[44, id_list[k]]
    temp_df['L45'] = matrix.at[45, id_list[k]]
    temp_df['L46'] = matrix.at[46, id_list[k]]
    temp_df['L47'] = matrix.at[47, id_list[k]]
    temp_df['L48'] = matrix.at[48, id_list[k]]
    temp_df['L49'] = matrix.at[49, id_list[k]]
    temp_df['L50'] = matrix.at[50, id_list[k]]
    for s in range(50):
        top = 'L' + str(s+1)
        check = check + sum(temp_df[top])
    print(check)
    index = list(data.index).index(id_list[k])
    print("index in meta data is:", index)
    temp_df['weather_group'] = [weather_list[index]] * 835
    temp_df['subscriber'] = data['ChannelDetails'][index]['ChannelSubscriberCount'] * 835
    published = list(data['PublishedAt'])[index]
    published_dates = abs(date(1970,1,1)- date(int(published[0:4]), int(published[5:7]), int(published[8:10]))).days
    nbw = (published_dates-base)/7
    print("The number of weeks since 2006 is: ", nbw)
    for weather in ['HW', 'FI', 'DR', 'HU', 'FL', 'NONE']:
        temp_df[weather] = time_weather_dict[weather]
    
    if (nbw < 835):
        published_ind = [0]* math.floor(nbw) + [1] * (835 - math.floor(nbw))
        life = [0]* math.floor(nbw) + list(range(835 - math.floor(nbw)))
    else:
        published_ind = [0] * 835
        life = [0] * 835
    
    
    temp_df['published'] = published_ind
    
    temp_df['life'] = life

    merge_list.append(temp_df)
    
    print('processing' + str(k))

hold_df = pd.concat(merge_list)

hold_df.to_csv('panel_1yr_50.csv')


hold_df = hold_df.reset_index(drop=True)

hold_df.to_json(r'panel_data_1yr_50.json')



