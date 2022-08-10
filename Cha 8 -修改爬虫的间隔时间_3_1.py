import requests
from bs4 import BeautifulSoup
import time
import random

link = "http://www.santostang.com/"

def scrap(link):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
    r = requests.get(link, headers= headers)
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    return soup

soup = scrap(link)
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    print ('start scap: ', url)
    soup_article = scrap(url)
    title = soup_article.find("h1", class_="view-title").text.strip()
    print ('title: ', title)
    sleep_time = random.randint(0,2) + random.random()
    print ('sleep: ', sleep_time, 's')
    time.sleep(sleep_time)