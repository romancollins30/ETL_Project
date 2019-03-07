# Import Dependecies 
from splinter import Browser
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import pymongo

# Initialize browser
def init_browser(): 
    # Replace the path with your actual path to the chromedriver

    #Windows Users
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # return Browser('chrome', **executable_path, headless=False)
    exec_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', headless=True, **exec_path)

data = {}

def scrape():
    browser = init_browser()
    url = 'https://www.mlb.com/'
    browser.visit(url)
    # HTML Object
    html = browser.html
    response = requests.get(url)
    soup = BeautifulSoup(html, 'html.parser')
    headline_title = soup.find('div', class_="mediawall__kicker-text").text

    results = soup.find('div', class_='mediawall__blurb')
    headline_body = results.p.text

    data['headline_title'] = headline_title
    data['headline_body'] = headline_body 

                
    # Visit Spring Training Schedule 
    standings_url = 'https://www.cbssports.com/mlb/standings/'

    # Use Panda's `read_html` to parse the url
    cactus_scores = pd.read_html(standings_url)

    # Find the cactus league DataFrame in the list of DataFrames
    standings_df = cactus_scores[1]

    # Save html code
    Cactus_League_Scores = standings_df.to_html()

    # Dictionary entry from MLB Scores
    data['mlb_scores'] = Cactus_League_Scores

    url = 'https://cactusleague.com/about.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html')
    cactus_title = soup.find('h2', class_="custom-underline").text

    cactus_body = soup.find('p').text
    # Dictionary entry from About Cactus
    data['cactus_title'] = cactus_title
    data['cactus_body'] = cactus_body
                

    #browser.is_element_present_by_css("img.jpg", wait_time=1)

    # Visit through splinter module
    image_url_featured = 'http://cactus-league.com/news/'
    browser.visit(image_url_featured)# Visit Mars Space Images through splinter module

    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('img')['src']

    # Display full link to featured image
    featured_image_url 

    # Dictionary entry from FEATURED IMAGE
    data['featured_image_url'] = featured_image_url 

    return data