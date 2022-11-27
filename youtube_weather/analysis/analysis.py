#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:11:41 2022

@author: maguo
"""


import pandas as pd

data = pd.read_json('topic_matrix.json')

output = pd.DataFrame(data.index)

output['ts'] = [[0]*835] *51


names = data.columns

for i in range(1140):
    vid = names[i]
    print('processing:' + vid)
    for j in range(51):
        print('processing data for characteristics ' + str(j))
        for k in range(835):
            output['ts'][j][k] = output['ts'][j][k] + data[vid][j][k] 
        
for i in range(51):
    output[0][i] = 'L' + str(i)
    
    
conct = []


count_df = pd.DataFrame()
count_df['time'] = range(835)
count_df['value'] = output['ts'][0]
count_df['name'] = output[0][0]

for i in range(1,51):
    temp_df = pd.DataFrame()
    temp_df['time'] = range(835)
    temp_df['value'] = output['ts'][i]
    for k in range(835):
        temp_df['value'][k] = temp_df['value'][k]/count_df['value'][k]
    temp_df['name'] = output[0][i]
    conct.append(temp_df)
    
    
hold_df = pd.concat(conct)

hold_df.to_csv('topics_analysis.csv')
    


    