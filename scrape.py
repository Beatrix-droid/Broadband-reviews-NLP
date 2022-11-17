#load relevant imports
from __future__ import annotations #for better type hints 

import requests
from bs4 import BeautifulSoup


#base url
BASE_URL="https://www.broadband.co.uk/broadband/providers/virgin-media/reviews/page:"

stars=[]
comments=[]
dates=[]

customer_service_reviews=[]
satisfaction_reviews=[]
speed_reviews=[]
reliability_reviews=[]


def scrape_data(page_number:int)-> BeautifulSoup:
    
    """returns an instance of the beatiful soup with the data scraped from the specified page"""

    url= BASE_URL +str(page_number)
    html_text=requests.get(url).text

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


for i in range(1, 50):
    soup=scrape_data(i)
    reviews = soup.find_all("li")

    for index, review in enumerate(reviews):
        try:
            
            comment= review.find("blockquote", class_="medium").text
            comment=comment.replace("\n", "")
            comment=comment.strip()

            comments.append(comment)
            date=review.find("dd", itemprop="datePublished")
        
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


print(len(comments))

