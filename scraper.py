#!pip install pandas requests BeautifulSoup4

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def scraper(url):
    article_paragraph = [] 
    response = requests.get(url)
    soup = bs(response.content, 'html.parser') 
    article_div = soup.findAll("article") 

    for j in range(len(article_div)):
        article_paragraph.append(article_div[j].text)
    
    article_word = []
    for i in range(len(article_paragraph)):
        article_word = article_paragraph[i].split()
    return article_word


# Driver code
Atricle1_words = scraper("https://www.focus-economics.com/countries/united-states/news/unemployment/labor-market-remains-strong-in-april")
i = range(1, len(Atricle1_words)+1)
article_df = pd.DataFrame({'words':Atricle1_words}, index=i)
article_df.to_csv('US5.txt', sep='t')
