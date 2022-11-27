#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:49:27 2022

@author: maguo
"""


import pandas as pd


df = pd.read_csv("topics.csv", encoding ="latin-1", header = None)

topic = set()

for i in range(480):
    for j in [4,5,6,7,8]:
        topic.add(df.at[i,j])
        

data = list(topic)
count = [0]*243
        
for i in range(480):
    for j in [4,5,6,7,8]:
        index = data.index(df.at[i,j])
        current_nb = count[index]
        count[index] = current_nb + 1
        
        
output = pd.DataFrame(data,columns=['word'])
output['Count'] = count

sort = output.sort_values(by='Count', ascending=False)

sort = sort.reset_index(drop=True)

top_q = sort[sort['Count']>24]

top_q['201601'] = [0]*24
top_q['201602'] = [0]*24
top_q['201603'] = [0]*24
top_q['201604'] = [0]*24
top_q['201701'] = [0]*24
top_q['201702'] = [0]*24
top_q['201703'] = [0]*24
top_q['201704'] = [0]*24
top_q['201801'] = [0]*24
top_q['201802'] = [0]*24
top_q['201803'] = [0]*24
top_q['201804'] = [0]*24
top_q['201901'] = [0]*24
top_q['201902'] = [0]*24
top_q['201903'] = [0]*24
top_q['201904'] = [0]*24
top_q['202001'] = [0]*24
top_q['202002'] = [0]*24
top_q['202003'] = [0]*24
top_q['202004'] = [0]*24
top_q['202101'] = [0]*24
top_q['202102'] = [0]*24
top_q['202103'] = [0]*24
top_q['202104'] = [0]*24


for k in range(24):
    word = top_q['word'][k]
    print(word)
    for year in [2016, 2017,2018,2019,2020,2021]:
        temp_df = df[df[0]==year]
        for quarter in [1, 2, 3, 4]:
            subdf = temp_df[temp_df[1] == quarter]
            subdf = subdf.reset_index(drop=True)
            name = str(year)+ "0" + str(quarter)
            count = 0
            for j in range(20):
                for i in [4,5,6,7,8]:
                    print(subdf.at[j,i])
                    if word == subdf.at[j,i]:
                        count = count + 1
            top_q[name][k] = count
        

top_q.to_csv('toptopic_freq_quarter.csv')

merge_list = []
index_list = list(top_q.columns)[2:]

for k in range(24):
    word = top_q['word'][k]
    temp_df = pd.DataFrame([word]*24)
    count = top_q['Count'][k]
    temp_df['Count'] = [count] * 24
    hold = [0]*24
    for i in range(24):
        hold[i] = top_q.at[k, index_list[i]]
    temp_df['Each_Count'] = hold
    
    merge_list.append(temp_df)

result_df = pd.concat(merge_list)


result_df.to_csv('toptopic_freq_quarter_wide.csv')

        
        
    
    


    
    