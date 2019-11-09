from bs4 import BeautifulSoup
from datetime import datetime 
import time 
import urllib 
import requests
import random 
import sys
import csv

# Function to make soup object
def make_soup(url):
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    read_html = html.read()
    soup = BeautifulSoup(str(read_html, "utf-8"), "html5lib")
    return soup

def get_article(article_cells, url):
    # Looping through all the aricles within the url
    current_list = []
    try:
        for article in article_cells:
            try:
                article_dict = {}

                # Set sleeping time 
                sleep_time = random.randint(1,5)
                print(f'Sleeping time {sleep_time}s')
                time.sleep(sleep_time)
                article_url = article.get('href')
                article_page = make_soup(article_url)
                print(f'Crawling article: {article_url}')

                # Retrieve Headline 
                headline = article_page.find(name="h1", class_="content__headline").get_text()
                if headline != None:
                    headline = headline.replace('\n', '')
                else: 
                    headline = article_page.find(name="h1", class_="content__headline content__headline--no-margin-bottom").get_text()
                    if headline != None:
                        headline = headline.replace('\n', '')
                    else:
                        headline = ''

                # Retrieve standfirst
                standfirst = article_page.find(name="div", class_="content__standfirst")
                if standfirst != None:
                    if standfirst.find('p') == None:
                        standfirst = standfirst.find('meta')
                        standfirst = standfirst.get('content')
                    else:
                        standfirst = standfirst.find('p').get_text()
                else:
                    standfirst = ''

                # Retrieve Author
                author = article_page.find(name="a", class_="tone-colour")
                if author != None: 
                    author =author.select('span')[0].get_text()
                else:
                    author = ''

                # Retreive content of the article
                all_content = article_page.find(name="div", class_="content__article-body from-content-api js-article__body")
                date_time = article_page.find(name="p", class_="content__dateline")
                if date_time != None:
                    date_time = date_time.find('time').get('datetime')
                else:
                    date_time = ''

                # Concat the list of paragraphs into a string of content
                content_string = ""
                for content in all_content.select('p'):
                    content_string += content.get_text()

                # Add all the retrieved data into a dictionary
                article_dict["headline"] = headline
                article_dict["standfirst"] = standfirst
                article_dict["author"] = author
                article_dict["date_time"] = date_time
                article_dict["content"] = content_string
                article_dict["url"] = article_url

                # Append the dictionary into a list and accumulate all the retrieved data
                current_list.append(article_dict)
                print(f'Successfully crawled article: {article_url}')

            except KeyboardInterrupt:
                print("Keyboard interrupted. Crawler will end ...")
                raise
            except Exception as e:
                print(f'Error occured when crawling second tab {article_url}')
                print("Error: {0}".format(sys.exc_info()))
    except KeyboardInterrupt:
        print("Keyboard interrupted. Crawler will end ...")
        raise
    except Exception as e:
        print(f'Error occured when crawling second tab {url}')
        print("Error: {0}".format(sys.exc_info()))
        # Export to csv
        keys = article_list[0].keys()
        with open(f'./data/the_guardian{today_date}incomplete.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(article_list)
        end_time = datetime.utcnow()
        print("Total time taken (mins): " +str(((end_time-start_time).total_seconds() / 60)))
    
    interval_time = datetime.utcnow()
    print("Total time taken (mins): " +str(((interval_time-start_time).total_seconds() / 60)))

    return current_list 

# Get start time with current date and time 
start_time = datetime.utcnow()
today_date = datetime.date(datetime.now())

# main_url = "https://www.theguardian.com/world/all"
first_part = 'https://www.theguardian.com/world?page=37'
second_part = 'https://www.theguardian.com/world?page=366'
# third_part = 'https://www.theguardian.com/world?page=401'
# fourth_part = 'https://www.theguardian.com/world?page=601'

main_page = make_soup(second_part)

# List to store all the crawled articles in dictionary form
article_list = []

# Crawling the individual cell of the article from the business main page 
article_cells = main_page.find_all(name="a", class_="u-faux-block-link__overlay js-headline-text")

print("_" * 60)
print(f'Accessing Page: {second_part}')
print("_" * 60)
article_list = get_article(article_cells, second_part)

next_page = main_page.find(name='a', class_='button button--small button--tertiary pagination__action--static', rel='next')
next_page = next_page.get('href')
next_page_number = next_page[next_page.find('page=')+5:]

count = 1

# [37-367], [366-771]
while(next_page != None and int(next_page_number) <= 771):
    next_page_soup = make_soup(next_page)
    next_page_cells = next_page_soup.find_all(name="a", class_="u-faux-block-link__overlay js-headline-text")

    print("_" * 60)
    print(f'Accessing Page: {next_page}')
    print("_" * 60)
    current_list = get_article(next_page_cells, next_page)
    article_list.extend(current_list)
    count += 1
    next_page = next_page_soup.find(name='a', class_='button button--small button--tertiary pagination__action--static', rel='next')
    next_page = next_page.get('href')
    next_page_number = next_page[next_page.find('page=')+5:]
   
# Export to csv
keys = article_list[0].keys()
with open(f'../news_data/the_guardian{today_date}_second_part.csv', 'w', encoding='utf-8-sig') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(article_list)
end_time = datetime.utcnow()
print("Total time taken (mins): " +str(((end_time-start_time).total_seconds() / 60)))