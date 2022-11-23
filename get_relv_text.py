#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:44:16 2022

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

"""

porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

"""
keywords = []
for lines in f.readlines():
    keywords.append(lines)
    

filelist = ["20191001_10-K-A_edgar_data_1127475_0001185185-19-001320.txt",
            "20191001_10-K-A_edgar_data_1127475_0001185185-19-001322.txt",
            "20191001_10-K-A_edgar_data_1528396_0001528396-19-000036.txt",
            "20191001_10-K_edgar_data_1020859_0001020859-19-000116.txt",
            "20191001_10-K_edgar_data_1061164_0001262463-19-000318.txt",
            "20191001_10-K_edgar_data_1365916_0001171843-19-006229.txt"]
test = ["20191001_10-K-A_edgar_data_1127475_0001185185-19-001320.txt"]

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
            print(inx)
            print(words)
            word_list.append(words)
            print(content[inx-150:inx+150])
            rev_text_list.append(content[inx-150: inx+150])
    
    data[file] = {
    'Name': company_name,
    'Industry': industry,
    'ISR_Number': isr_nub,
    'Time': file[:7],
    'Year': year,
    'Quarter': quarter,
    'Count': count,
    'Words': word_list,
    'Rev_Text': rev_text_list}
            

with open(f'exact/rev{year}q{quarter}.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))

with open(f'exact/exact.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))
    

with open(f'exact/revprob{year}q{quarter}.json','a') as fout:
    for item in problem:
        fout.write(item + "\n")

"""   

with open('rev2020q4.json','a') as fout:
    fout.write(json.dumps(data, indent = 2))
    

with open('revprob2020q4.json','a') as fout:
    for item in problem:
        fout.write(item + "\n")
"""        
    
