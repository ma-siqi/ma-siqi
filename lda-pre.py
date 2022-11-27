#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:55:27 2022

@author: maguo
"""

import json
import re
import sys

year = str(sys.argv[1])
quarter = str(sys.argv[2])
quarter_str = 'QTR' + quarter

path_name = year + "q" + quarter + "ls"

data_list = {}


with open(f"lists/{year}/{path_name}.txt","r") as ls:
    for lines in ls:
        data_list[str(lines).rstrip()] = ""

keywords = ['environment','environmental','climate','sustainability','sustainable']

data = {}
problem = []
for file in data_list:
    doc = open(f'data/{year}/{quarter_str}/{file}')
    content = doc.read().strip()
    removed = content.replace("\r", "").replace("\n", "")
    try:
        company_name = re.search('COMPANY CONFORMED NAME:.*', content).group(0)
        print(company_name)
        industry = re.search('STANDARD INDUSTRIAL CLASSIFICATION:.*', content).group(0)
        print(industry)
        isr_nub = re.search('IRS NUMBER:.*', content).group(0)
        print(isr_nub)
            
    except:
        problem.append(file)
        continue
    
    count = 0
    rev_text_list = []
    word_list = []
    for words in keywords:
        if words in content:
            count = count + 1
            print(count)
            inx = content.index(words)
            word_list.append(words)
            print(inx)
            print(words)
            print(content[inx-150:inx+150])
            rev_text_list.append(content[inx-150: inx+150])
    
    data[file] = {
    'Name': company_name,
    'Industry': industry,
    'ISR_Number': isr_nub,
    'Time': file[:7],
    'Count': count,
    'Words': word_list,
    'Rev_Text': rev_text_list}
            
    

with open(f'lda/rev{year}q{quarter}.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))

with open(f'lda/lda_pre.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))
    

with open(f'lda/revprob{year}q{quarter}.json','a') as fout:
    for item in problem:
        fout.write(item + "\n")
    
