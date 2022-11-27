#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:03:17 2022

@author: maguo
"""


import re
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


data_list = {}

with open("no.txt","r") as ls:
    for lines in ls:
        data_list[str(lines).rstrip()] = ""
        

filelist = ["20211001_10-K_edgar_data_1338929_0001477932-21-006965.txt",
            "20211001_10-K_edgar_data_732026_0001654954-21-010701.txt",
            "20211001_10-Q_edgar_data_1164888_0001493152-21-024269.txt",
            "20211001_10-Q_edgar_data_1170010_0001170010-21-000179.txt",
            "20211001_10-Q_edgar_data_1267919_0001376474-21-000333.txt",
            "20211001_10-Q_edgar_data_1498232_0001214659-21-009985.txt",
            "20211001_10-Q_edgar_data_1498232_0001214659-21-009993.txt",
            "20211001_10-Q_edgar_data_1498232_0001214659-21-009995.txt"]

testlist = ["20211001_10-Q_edgar_data_1164888_0001493152-21-024269.txt"]

data = {}

problem = []

porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

def stemKeywords():
    f = open("env_policy_kw.txt")
    keywords = []
    for lines in f.readlines():
        keywords.append(stemSentence(lines))
    
    return keywords

keywords = stemKeywords()
    

for file in data_list:
    doc = open(f'2021/{file}')
    content = doc.read().strip()
    removed = content.replace("\r", "").replace("\n", "")
    try:
        company_name = re.search('COMPANY CONFORMED NAME:.*', content).group(0)
        print(company_name)
        industry = re.search('STANDARD INDUSTRIAL CLASSIFICATION:.*', content).group(0)
        print(industry)
        isr_nub = re.search('IRS NUMBER:.*', content).group(0)
        print(isr_nub)
            
        data[file] = {
            'Name': company_name,
            'Industry': industry,
            'ISR_Number': isr_nub,
            'Time': file[:7],
            'Text': removed}
    except:
        problem.append(file)
        continue
    
    #get policy word stemming match
    linelist = doc.readlines()
    for lines in linelist:
        
    
        
        
#print(data)

with open('data_test2.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))

with open('problem2.json','a') as fout:
    for item in problem:
        fout.write(item)

        
