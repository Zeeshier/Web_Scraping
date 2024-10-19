import os
import subprocess
import sys
import requests
from bs4 import BeautifulSoup
import lxml
from lxml import html

#Fetch the webpage
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

#check if the request was successful
if response.status_code == 200:
    
    #parse the Html content
    page = BeautifulSoup(response.content, 'lxml')
    quotes = page.find_all('span', class_='text')
    authors = page.find_all('small', class_='author')

    #print the quotes
    for i in range(len(quotes)):
        print(quotes[i].text)
        print(authors[i].text)
        print()
else:
    print('Error fetching the webpage')

