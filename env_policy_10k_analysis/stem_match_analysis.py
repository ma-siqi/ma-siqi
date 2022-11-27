#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:01:41 2022

@author: maguo
"""


import json

import pandas as pd

"""
data = pd.read_json('exact_data.json').T

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
    
    
data.to_csv('exact_clean.csv', index=False)  

stem = pd.read_csv('stem_clean.csv')
exact = pd.read_csv('exact_clean.csv')


stem_sort = stem.sort_values(by='Industry', ascending=False)
stem_sort = stem_sort.reset_index(drop=True)
exact_sort = exact.sort_values(by='Industry', ascending=False)
exact_sort = exact_sort.reset_index(drop=True)

temp_df = stem_sort
temp_df['Exact_Count'] = exact_sort['Count']

temp_df.to_csv('match.csv')

"""

temp_df = pd.read_csv('match.csv') 


ind_dic= json.load(open('industry/industry_dic_new.json'))


l1 = []
l2 = []
l3 = []
l4 = []
prob = []
for i in range(164431):
    ind = str(temp_df['Industry'][i])
    #print(ind)
    try:
        l1.append(ind_dic[ind]['Level_1'])
        l2.append(ind_dic[ind]['Level_2'])
        l3.append(ind_dic[ind]['Level_3'])
        l4.append(ind_dic[ind]['Level_4'])
    except:
        ind_new = ind[:3]
        print(ind_new)
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


    
temp_df['level1']= l1
temp_df['level2'] = l2
temp_df['level3'] = l3
temp_df['level4'] = l4

temp_df.to_csv('match_clean.csv')





