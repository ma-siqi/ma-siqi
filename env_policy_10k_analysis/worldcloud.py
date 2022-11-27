#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:20:55 2022

@author: maguo
"""


# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
df = pd.read_csv("topic_words.csv", encoding ="latin-1", header = None)


comment_words = ""
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        print(df.at[i,j])
        comment_words += " "+ df.at[i,j]

wordcloud = WordCloud(width = 1000, height = 800,
				background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)

# plot the WordCloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Create a random number generator with a fixed seed for reproducibility
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(dist1, bins=n_bins)
