#load relevant imports
from __future__ import annotations #for better type hints 
import pandas as pd


import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import os
from dotenv import load_dotenv


load_dotenv()
#base url from which to construct the one used by scraping function
BASE_URL="https://www.broadband.co.uk/broadband/providers/virgin-media/reviews/page:"


#modify headers to prevent getting blocked by website
HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept-Language":  "en-GB,en;q=0.8",
"Referer": "https://google.com",
"DNT":"1"}

stars=[]
comments=[]
dates=[]

customer_service_reviews=[]
satisfaction_reviews=[]
speed_reviews=[]
reliability_reviews=[]

list_of_urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/2/']

 
def scrape_data(page_number:int)-> BeautifulSoup:
    
    """returns an instance of the beautiful soup with the data scraped from the specified page"""

    url= BASE_URL +str(page_number)
    params = {'api_key': os.getenv("API_KEY"), 'url': url}
    html_text = requests.get('http://api.scraperapi.com/', params=urlencode(params))
    html_text=requests.get(url, headers=HEADERS).text

    soup = BeautifulSoup(html_text, 'html.parser')
    return soup




def obtain_lists(index: int, list_to_put_it_in: list) -> None:
    
    """Helper function that avoids code repetition. Scrapes from a list of objects, parses 
    the text and puts them in the correct list"""
    
    scraped_text=rating[index].span.text
    scraped_text=scraped_text[0]
    scraped_text=float(scraped_text)
    list_to_put_it_in.append(scraped_text)



#use this loop to process the text reviews. Extract and clean them from the unnecessary html tags


for i in range(1, 110):
    soup=scrape_data(i)
    reviews = soup.find_all("li")
   

    for index, review in enumerate(reviews):
        try:
            
            comment= review.find("blockquote", class_="medium").text
            comment=comment.replace("\n", "")
            comment=comment.strip()

            comments.append(comment)
            date=review.find("dd", itemprop="datePublished").text
            date=date.replace("\t", "")
            date=date.replace("\n","")
            dates.append(date)
    
        except:
            pass

    #this main loop will go through all the different ratings gathered in teh she soup
    ratings=soup.find_all("ul", class_="ratings")

    for index, rating in enumerate(ratings):
        rating = rating.find_all("li")

        obtain_lists(0, satisfaction_reviews)
        if len(rating)>1:
            obtain_lists(1, customer_service_reviews)

        if len(rating)>2:
            obtain_lists(2, speed_reviews)

        if len(rating)>3:
            obtain_lists(3, reliability_reviews)

#first item of the list is a bit off so delete it 

del customer_service_reviews[0]
del satisfaction_reviews[0]
del speed_reviews[0]
del reliability_reviews[0]

df_dict={"Dates": dates, "Comments": comments, "Customer Service": customer_service_reviews, "Satisfaction Reviews": satisfaction_reviews, "Speed Reviews": speed_reviews, "Reliability Reviews": reliability_reviews}

#as certain columns are shorter than others use a trick to create a df with unequal arrays:https://stackoverflow.com/questions/19736080/creating-dataframe-from-a-dictionary-where-entries-have-different-lengths
df = pd.DataFrame.from_dict(df_dict, orient='index')
df=df.transpose()

#convert the dates columns from string to datetime object:
df["Dates"]= pd.to_datetime(df["Dates"])

#save date to csv:
df.to_csv('./data/raw_data.csv')




