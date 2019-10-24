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

# Get start time with current date and time 
start_time = datetime.utcnow()
today_date = datetime.date(datetime.now())

main_url = "https://www.theguardian.com/international"
main_page = make_soup(main_url)
first_tabs = main_page.find_all(name="li", class_="pillars__item")

# Store all the url links into a list
tabs_list = []
for first_tab in first_tabs:
    first_tab_url = first_tab.find(name="a").get('href')
    first_tab_page = make_soup(first_tab_url)
    second_tabs = first_tab_page.find_all(name="li", class_="subnav__item")
    for second_tab in second_tabs:
        second_tab_text = second_tab.find('a').get_text()
        tabs_list.append(second_tab.find(name="a", class_="subnav-link").get('href'))
        # print(second_tab_text, second_tab.find(name="a", class_="subnav-link").get('href'))

# Remove duplicate from the list 
tabs_list = list(set(tabs_list))

# List to store all the crawled articles in dictionary form
article_list = []

# Main loop to loop through all the url links which store multiple articles
for tab in tabs_list:
    main_page = make_soup(tab)
    # Crawling the individual cell of the article from the business main page 
    article_cells = main_page.find_all(name="a", class_="u-faux-block-link__overlay js-headline-text")

    print("-" * 60)
    print(f'Accessing page: {tab}')
    print("-" * 60)
    try: 
        # Looping through all the aricles within the url
        for article in article_cells:
            try:
                article_dict = {}

                # Set sleeping time 
                sleep_time = random.randint(1,7)
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

                # Append the dictionary into a list and accumulate all the retrieved data
                article_list.append(article_dict)
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
        print(f'Error occured when crawling second tab {tab}')
        print("Error: {0}".format(sys.exc_info()))

    interval_time = datetime.utcnow()
    print("Total time taken (mins): " +str(((interval_time-start_time).total_seconds() / 60)))

# Export to csv
keys = article_list[0].keys()
with open(f'./data/the_guardian{today_date}.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(article_list)
end_time = datetime.utcnow()
print("Total time taken (mins): " +str(((end_time-start_time).total_seconds() / 60)))