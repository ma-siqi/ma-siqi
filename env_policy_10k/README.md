# NLP methods in understanding 10K/10Q form and environmental policy impact

This project aims at developing a reliable NLP analysis framework through which SIC companies' responses to environmental policy can be analyzed by applying the framework on their 10K/10Q forms.

## Scripting 10K/10Q form from SIC EDGAR databse

## Topic analysis

The goal of performing topic analysis is to understand what firms are talking about when they mentioned sustainability and environmental issues.

### Pre-topic filtering

A neightborhood of text around words like "environment", "sustainability" is used to identify conversation about environmental issues.
Create a folder named LDA, then rename it to lda-pre after running.

(lda-pre.py) and (run_lda.sh)

### LDA
This is the topic model to start with, k is chosen to be 20 to avoid missing topics.
Create a folder named LDA

(lda.py) and (run-lda-post.sh)

### BERT topic
The BERT model can be applied to generate seed-based and hierarchical modeling.

(TBD)

### Topic analysis

Topics are put into long csv format by year and quarters.

Analysis is performed by breaking down industry, sunindustry, and time trend.

(topic_analysis.py) and (topic_analysis.rmd)

## Keyword model
A list of 454 environmental policy keywords is used initially. 100 random samples is used to test whether the match captures relevant discussion. Zoning and audit is removed because it creates large amount of noise.

### Exact match
 
(get_relv_text.py) and (run-exact.sh)

### Stemming word match

(teststem.py) and (run-stem.sh)

