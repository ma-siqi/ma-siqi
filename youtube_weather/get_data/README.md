# Youtube Video Data Collection Scripts
This folder contains scripts used to collect youtube video data for further analysis. They can get keyword search results from youtube search, get metadata, filter out unuseful videos, get channel-related details, get comments, and get recommended videos.

## The process for scraping metadata, recommendations, comments, and analysis
The whole process to get useful data is the following:
1. Get keyword search result.
2. Get metadata NOT using youtube API (to save API use limit). This metadata is not as detailed, but we can use this result to filter out videos according to our citeria (for now, the citeria is that we will not use videos without description or is private).
3. Get the url for those filtered data so that we can use them as input to youtube API to get detailed metadata.
4. Get detailed metadata from youtube API.
5. Do description exact matching to get a better quality.
6. Run com_scrapper to get comments.
7. Run rec_scraper to get recommended videos. (Calculate the number of recommended videos that is also in the video list?)
8. Run transcript to get video transcripts.
9. Data analysis.

## 1. Get keyword search result: search_keyword.py
The script will take a input of .txt file with each line being a keyword, put the keyword to youtube search, and save all the video that appear as search results to a .json file.

### How to use:
You need to have chromedriver.
In line 17, it says:
```python
driver = webdriver.Chrome(executable_path='/Users/maguo/Desktop/scrapers_yt/chromedriver')
```
Run the script, you should get the result stored in search_result.txt

###Things to notice:
1. The program has two stages: it first get all chromedriver results, then it analyze the result and stores them. If you put chromedriver into the background while it is getting results, it is running very slow. So don't use your computer when chromedriver is driving chrome. Also, if the computer sleeps, chromedriver will be interrupted and python will stop. When it reaches the end, python is analyzing the result, you can use computer now. Sleeping computer in this stage will not stop the program.
2. The program ADDS to the output json. So if your program stopped, you can just remove what's already being searched from the input file and run it again.
3. Result json: The output is not strictly a json, because for each keyword, we are starting a new {}. To change it to a strict json, search for all "}{" and replace it with ",".

After this step, you should get a search_result.json file

##2. Get metadata (simplified): tidy_id.py, meta_scraper.py
The script will extract html file of the video and get the information from that page. It cannot get full description because description is often folded. Channel results is also not getten because they are not displayed. But this is sufficient to get a simplified version that we can filter out.

It takes a list of video url and outputs the meta data to a json.

###How to use  

Before all these, remember to search for all "}{" in x.json from previous step and replace them with ",". Otherwise, json will have an error.

Run tidy_id.py, result is stored in url.txt

Run meta_scraper.py, You should get meta1.json file.

###Things to notice:
1. The program ADDS to the output json. So if your program stopped, you can just remove what's already being searched from the input file and run it again.
2. Result json: The output is not strictly a json, because for each keyword, we are starting a new {}. To change it to a strict json, search for all "}{" and replace it with ",".

##3: Filter data: filter.py
This takes in the json result from previous process, filtered out unuseful videos, and stores them.

Run filter.py, result is stored in filtered_url_list.txt

##4: Get detailed metadata from Youtube API: meta_new.py
To do this step, you need a youtube API key and google developer account.

###Register for Google Developer:
1. Go to this link: https://cloud.google.com/, follow the instruction to register for an account.
2. Once registered, go to https://console.cloud.google.com/. Create a project.
3. Goto the menu (3 horizontal line) on the left top of the page. Goto API Service -> library. Search for youtube data api v3. Enable this API.
4. Go to home page again (https://console.cloud.google.com/), go to Menu -> API service -> Enabled APIs & service -> credentials, click create credentials -> API key. You should get an API key.

###How to use python:
In line 13:
```python
DEVELOPER_KEY = 'AIzaSyDG2XqteQKyQ-BcYT3l3sap7PQqNLG6oks'
```
change DEVELOPER_KEY to your own key.

Run meta_new.py, the final result is in meta_filtered.json. 

###Things to notice:
1. There will be API key limits per day.

##5. Description exact match with keywords
Use term_match.py.

