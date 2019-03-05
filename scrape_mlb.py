


from bs4 import BeautifulSoup
import requests
import pymongo


def scrape():
    url = 'https://www.mlb.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html')
    headline_title = soup.find('div', class_="mediawall__kicker-text").text


    results = soup.find('div', class_='mediawall__blurb')
    headline_body = results.p.text

    print(headline_body)
    data = {
        'headline_title' : headline_title,
        'headline_body' : headline_body 
    }

    return data


