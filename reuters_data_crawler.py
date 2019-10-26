from bs4 import BeautifulSoup
from datetime import datetime 
import time 
import urllib 
import requests
import random 
import csv
import sys

# Function to define BSoup Object

def create_soup(url):

    # Can use requests.get("url")
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    html_doc = html.read()
    # html5lib for parsing html
    soup = BeautifulSoup(str(html_doc, "utf-8"), "html5lib")
    return soup

# Get start time with current date and time
start_time = datetime.utcnow()
today_date = datetime.date(datetime.now())

reuters_news_data_url_list = []

# start loop from page 1 to page 1110
    reuters_news_data_url_list.append("https://www.reuters.com/news/archive/businessnews?view=page&page=" + str(i) + "&pageSize=10")

# print(reuters_news_data_url_list)

web = "https://www.reuters.com"

reuters_articles_url_list  = []

master_list = []

# For loop to access each url
try:
    for url in reuters_news_data_url_list:
        reuters_news_data = create_soup(url)
        # print(reuters_news_data)
        news_data = reuters_news_data.find_all(name = 'div', class_= 'story-content')
        # <class 'bs4.element.ResultSet'>
        # print(type(news_data)) 

        print("_" * 60)
        print(f'Accessing Page: {url}')
        print("_" * 60)
        
        # sleep_time = random.randint(1,4)
        # print(f'Sleeping time: {sleep_time} seconds')
        # time.sleep(sleep_time)

        try:
            for item in news_data:
                article = {}
                each_link = web + item.select('a')[0].get('href')

                sleep_time = random.randint(1,3)
                print(f'Sleeping time: {sleep_time} seconds')
                time.sleep(sleep_time)
                print(f'Crawling page: {each_link}')

                article_data = create_soup(each_link)
                
                #Headline
                article_headline_data = article_data.find("h1")
            
                #Date
                article_date_data = article_data.find(name = "div", class_ = "ArticleHeader_date")
                
                p_content_string = ""

                #Article Main Body 
                article_main_body_data = article_data.find(name = "div", class_ = "StandardArticleBody_body")
                article_main_body_data_p = article_main_body_data.select("p")
                num_of_p = len(article_main_body_data_p)

                for j in range(num_of_p-1):
                    p_content_string = p_content_string + article_main_body_data_p[j].get_text()


                article['headline'] = article_headline_data.get_text()
                article['date'] = article_date_data.get_text()
                article['content'] = p_content_string

                master_list.append(article)

                print(f'Successfully crawled {each_link}')
                print("*" * 40)
            # print(master_list)

        except Exception as e:
            print(f'Error occured when crawling page {item}')
            print("Error: {0}".format(sys.exc_info()))
        interval_time = datetime.utcnow()
        print("Total time taken (mins): " +str(((interval_time-start_time).total_seconds() / 60)))


except Exception as e:
        print(f'Error occured when crawling page {url}')
        print("Error: {0}".format(sys.exc_info()))

keys = master_list[0].keys()
with open(f'./data/reuters{today_date}.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(master_list)

# keys = master_list[0].keys()
# with open(f'./data/reuters{today_date}darren.csv', 'a+', newline='') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
# #     dict_writer.writeheader()
#     dict_writer.writerows(master_list)

end_time = datetime.utcnow()
print("Total time taken (mins): " +str(((end_time-start_time).total_seconds() / 60)))