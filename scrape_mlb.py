


from bs4 import BeautifulSoup
import requests
import pymongo


def scrape():
    url = 'https://www.mlb.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html')
    headline = soup.find('div', class_="mediawall__panel mediawall__panel--news")


    url = 'https://www.mlb.com/news/2018-19-mlb-offseason-analysis-for-each-move-c302712514?t=trade-talk-and-rumors'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    articles = soup.find_all('li', class_="article-navigation__item")

    data = {
        'headline' : headline,
        'article' : articles[0] 
    }

    return data


