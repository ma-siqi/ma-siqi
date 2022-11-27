#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:56:39 2022

@author: maguo
"""

import pandas as pd
from datetime import date

time = pd.read_csv('Diasters.csv')

date1 = date(2006,1,1)

weeks_from = []
weeks_to = []


for i in range(time.shape[0]):
    datelist = time.at[i,'date'].split('.')
    date2 = date(int(datelist[0]), int(datelist[1]), int(datelist[2]))
    days = abs(date1-date2).days
    weeks_from.append(days/7)
    weeks_to.append(days/7 + 52)

time['from'] = weeks_from
time['to'] = weeks_to

time.to_csv('diaster_nbw_1y.csv')