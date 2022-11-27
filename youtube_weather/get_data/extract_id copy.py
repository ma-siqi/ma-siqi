#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:39:50 2022

@author: maguo
"""

import json

file = open('matched_tagged.json')
metadata = json.load(file)

keylist = []

for keys in metadata:
    keylist.append(keys)
    
with open('matched_url.txt','a') as fout:
    for item in keylist:
        fout.write(item + '\n')  