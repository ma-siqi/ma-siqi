#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:25:48 2022

@author: maguo
"""

import json

file = open('meta1.json')
metadata = json.load(file)

isPrivate = False
noDescription= False

filtered = dict(metadata)


for keys in metadata:
    print(keys)
    if metadata[keys]['type'] == 'public':
        isPrivate = False
        if metadata[keys]['description'] == "\"\"":
            noDescription = True
        else:
            noDescription = False
    else:
        isPrivate = True
        
    
    if noDescription or isPrivate:
        print("Filtered out " + keys)
        filtered.pop(keys)
        
with open('filtered1.json', 'a') as fout:
    fout.write(json.dumps(filtered, indent = 2))
    
keylist = []
for keys in filtered:
    keylist.append(keys)
    
with open('filtered_url_list.txt','a') as fout:
    for item in keylist:
        fout.write(item + '\n')  
#des = metadata['-2IBXeypbmU']['description']
