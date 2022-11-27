#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:35:13 2022

@author: maguo
"""

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
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

f = open("env_policy_kw.txt")


porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


keywords = []
for lines in f.readlines():
    keywords.append(stemSentence(lines))
    

    
filelist = ["20211001_10-K_edgar_data_1338929_0001477932-21-006965.txt",
            "20211001_10-K_edgar_data_732026_0001654954-21-010701.txt",
            "20211001_10-Q_edgar_data_1164888_0001493152-21-024269.txt",
            "20211001_10-Q_edgar_data_1170010_0001170010-21-000179.txt",
            "20211001_10-Q_edgar_data_1267919_0001376474-21-000333.txt",
            "20211001_10-Q_edgar_data_1498232_0001214659-21-009985.txt",
            "20211001_10-Q_edgar_data_1498232_0001214659-21-009993.txt",
            "20211001_10-Q_edgar_data_1498232_0001214659-21-009995.txt"]


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
    
    doc = open(f'data/{year}/{quarter_str}/{file}').readlines()
    stem_file = []
    for lines in doc:
        stem_file.append(stemSentence(lines))
        
    textbody = "".join(stem_file)
    count = 0
    rev_text_list = []
    word_list = []
    for words in keywords:
        if words in textbody:
            count = count + 1
            inx = textbody.index(words)
            word_list.append(words)
            rev_text_list.append(textbody[inx-200: inx+200])
    
    print(count)
    data[file] = {
    'Name': company_name,
    'Industry': industry,
    'ISR_Number': isr_nub,
    'Time': file[:7],
    'Year': year,
    'Quarter': quarter,
    'Words': word_list,
    'Count': count}
            
with open(f'stem/rev{year}q{quarter}.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))

with open(f'stem/stem.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))
    

with open(f'stem/revprob{year}q{quarter}.json','a') as fout:
    for item in problem:
        fout.write(item + "\n")

"""  

with open('dataset_match2019q4.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))
    

with open('stem_problem2019q4.json','a') as fout:
    for item in problem:
        fout.write(item + "\n")
    
"""
