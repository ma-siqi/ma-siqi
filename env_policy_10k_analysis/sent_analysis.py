#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:35:21 2022

@author: maguo
"""


import json

import pandas as pd
"""

data = pd.read_json('sentiment_exact.json').T

for i in range(164431):
    string_indus= data['Industry'][i]
    number = string_indus[-5:-1]
    print(number)
    data['Industry'][i] = number
    
for i in range(164431):
    string_indus= data['ISR_Number'][i]
    number = string_indus[-9:]
    print(number)
    data['ISR_Number'][i] = number
    
    
for i in range(164431):
    name = data['Name'][i]
    company_name = name[26:]
    print(company_name)
    data['Name'][i] = company_name
    
df = data.drop('Rev_Text', axis=1)
df= df.drop('pip', axis=1)



df.to_csv('sentiment.csv', index=False)  

import math
is_zero = df[-pd.isna(df['Avg_Sent'])]

not_zero = is_zero[is_zero['Avg_Sent']!=0]

not_zero.to_csv('nonzero_sent.csv')

"""

data = pd.read_csv('nonzero_sent.csv')

ind_dic= json.load(open('industry/industry_dic_new.json'))


l1 = []
l2 = []
l3 = []
l4 = []
prob = []
for i in range(6543):
    ind = str(data['Industry'][i])
    print(ind)
    try:
        l1.append(ind_dic[ind]['Level_1'])
        l2.append(ind_dic[ind]['Level_2'])
        l3.append(ind_dic[ind]['Level_3'])
        l4.append(ind_dic[ind]['Level_4'])
    except:
        ind_new = ind[:3]
        try:
            l1.append(ind_dic[ind_new]['Level_1'])
            l2.append(ind_dic[ind_new]['Level_2'])
            l3.append(ind_dic[ind_new]['Level_3'])
            l4.append(ind_dic[ind_new]['Level_4'])
        except:
            l1.append("No Industry Found")
            l2.append("No Industry Found")
            l3.append("No Industry Found")
            l4.append("No Industry Found")
            prob.append(ind)


    
data['level1']= l1
data['level2'] = l2
data['level3'] = l3
data['level4'] = l4

data.to_csv('nonzero_sent_ind.csv')


"""
most = []
most_desc = []
upper_list = []
upper_desc = []
middle_list = []
for i in range(6543):
    ind = str(data['Industry'][i])
    most.append(ind[:1])
    upper_list.append(ind[:2])
    middle_list.append(ind[:3])
    
data['level1']= most
data['level2'] = upper_list
data['level3'] = middle_list
    
data.to_csv('nonzero_sent_ind.csv')
"""