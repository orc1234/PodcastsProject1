import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import time
time.sleep(3)

# Crawling step 1 - Extract podcast data from https://www.listennotes.com/

# This function gets a class page and return all podcasts links which located at this specific page.
def insert_to_dict(podcasts_soup,podcast_dictionary):
    for card in podcasts_soup.find_all('div', class_="ln-page-card"):
        related_class = card.find('div',class_="grid grid-cols-1 gap-2 md:gap-4")
       # related_class2 = card.find('div', class_="grid grid-cols-1 gap-2 md:gap-4")
        if related_class is not None:
            link_to_podcast = related_class.find('a', class_="line-clamp-1")
            podcast_name = related_class.find('a', class_="line-clamp-1")
            writer = related_class.find('a', class_="ml-1 text-black inline")
            if podcast_name is not None:
                podcasts_url = link_to_podcast.get('href')
                headers = {'User-Agent': 'Chrome/96.0.4664.110'}
                response_podcasts = requests.get(podcasts_url,headers=headers)
                current_podcasts_soup = BeautifulSoup(response_podcasts.content, "html.parser")
                podcast_dictionary['podcast_name'].append(podcast_name.text.strip())
                podcast_dictionary['link'].append(link_to_podcast.get('href'))
                if writer is not None:
                    podcast_dictionary['writer'].append(writer.text.strip())
                else:
                    podcast_dictionary['writer'].append(None)
                top_rank = ""
                listen_score = ""
                for podcast in current_podcasts_soup.find_all('div', class_="ln-page-card"):
                    related_class3 = podcast.find('div', class_="flex mt-8 text-helper-color text-sm flex-wrap")
                    related_class4 = podcast.find('div', class_="text-center grid grid-cols-1 gap-4")
                    if related_class3 is not None:
                        language = related_class3.find_all('div', class_="flex items-center mb-4")[0]
                        if language is not None:
                            podcast_dictionary['language'].append(language.text.strip())
                        else:
                            podcast_dictionary['language'].append(None)
                        country = related_class3.find_all('div', class_="flex items-center mb-4")[1]
                        if country is not None:
                            podcast_dictionary['country'].append(country.text.strip())
                        else:
                            podcast_dictionary['country'].append(None)
                        episodes = related_class3.find_all('div', class_="flex items-center mb-4")[2]
                        if episodes is not None:
                            podcast_dictionary['episodes'].append(episodes.text.strip())
                        else:
                            podcast_dictionary['episodes'].append(None)
                        publish_date = related_class3.find('div', class_="flex items-center whitespace-nowrap mb-4")
                        if publish_date is not None:
                            podcast_dictionary['publish_date'].append(publish_date.text.strip())
                        else:
                            podcast_dictionary['publish_date'].append(None)

                        cat_list = []
                        podcast_dictionary['category'].append(cat_list)
                        for cat in current_podcasts_soup.find_all('div', class_="mr-2 mb-2"):
                            category = cat.find('a', class_="py-1 px-2 bg-bggray-color rounded shadow text-sm font-semibold hover:opacity-50 whitespace-nowrap")
                            if category is not None:
                                cat_list.append(category.text.strip())
                            else:
                                podcast_dictionary['category'].append(None)

                    if related_class4 is not None:
                        related_class4 = podcast.find_all('div', class_="text-center grid grid-cols-1 gap-4")[0]
                        listen_score = related_class4.find_all('div', class_="ln-listen-score-number ln-l1-text")[0]
                        if listen_score is not None:
                            podcast_dictionary['ListenScore'].append(listen_score.text.strip().split()[1])
                        else:
                            podcast_dictionary['ListenScore'].append(None)
                        related_class4 = podcast.find_all('div', class_="text-center grid grid-cols-1 gap-4")[1]
                        top_rank = related_class4.find_all('div', class_="ln-listen-score-number ln-l1-text")[0]
                        if top_rank is not None:
                            podcast_dictionary['top_rank'].append(top_rank.text.strip().split()[1])
                        else:
                            podcast_dictionary['top_rank'].append(None)

                if top_rank == "":
                    podcast_dictionary['top_rank'].append(None)
                if listen_score == "":
                    podcast_dictionary['ListenScore'].append(None)
            else:
                podcast_dictionary['podcast_name'].append(None)
                podcast_dictionary['link'].append(None)
                podcast_dictionary['writer'].append(None)
# This function creates a podcast list by month for 2019
def create_podcast_list_by_month_2019(podcast_dictionary):
    for m in range(1, 13):
        for d in range(1, 18):
            a_date = (datetime.date(2019, m, d)).isoformat()
            podcasts_url = "https://www.listennotes.com/hot-podcasts/" + a_date + "/#podcasts"
            response_podcasts = requests.get(podcasts_url)
            podcasts_soup_2019 = BeautifulSoup(response_podcasts.content, "html.parser")
            insert_to_dict(podcasts_soup_2019,podcast_dictionary)
# This function creates a podcast list by month for 2020
def create_podcast_list_by_month_2020(podcast_dictionary):
    for m in range(1, 13):
        for d in range(1, 18):
            a_date = (datetime.date(2020, m, d)).isoformat()
            podcasts_url = "https://www.listennotes.com/hot-podcasts/" + a_date + "/#podcasts"
            response_podcasts = requests.get(podcasts_url)
            podcasts_soup_2020 = BeautifulSoup(response_podcasts.content, "html.parser")
            insert_to_dict(podcasts_soup_2020,podcast_dictionary)
# This function creates a podcast list by month for 2021
def create_podcast_list_by_month_2021(podcast_dictionary):
    for m in range(1, 13):
        for d in range(1, 18):
            a_date = (datetime.date(2021, m, d)).isoformat()
            podcasts_url = "https://www.listennotes.com/hot-podcasts/" + a_date + "/#podcasts"
            response_podcasts = requests.get(podcasts_url)
            podcasts_soup_2021 = BeautifulSoup(response_podcasts.content, "html.parser")
            insert_to_dict(podcasts_soup_2021,podcast_dictionary)
def extract_all_podcast(podcast_dictionary):
    create_podcast_list_by_month_2019(podcast_dictionary)
    create_podcast_list_by_month_2020(podcast_dictionary)
    create_podcast_list_by_month_2021(podcast_dictionary)

# main()
podcast_dictionary = {'podcast_name': [],'writer': [], 'link': [], 'language': [], 'country': [], 'category': [], 'episodes': [], 'publish_date': [], 'ListenScore': [], 'top_rank': []}
extract_all_podcast(podcast_dictionary)
df_podcast = pd.DataFrame(podcast_dictionary)
df_podcast.to_csv('podcasts.csv')


