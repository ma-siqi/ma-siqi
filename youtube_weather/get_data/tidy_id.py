#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:46:43 2022

@author: Siqi Ma

This script is used to tidy-up json and output url lists
"""

import json

f = open('search_result.json')

data = json.load(f)

url_list = []

for item in data:
    url = data[item]["link"]
    url_list.append(url)
    

with open('url.txt','a') as fout:
    for item in url_list:
        fout.write(item + '\n')


    

