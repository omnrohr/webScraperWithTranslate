from random import randint
import time
from bs4 import BeautifulSoup as BS
import csv
import requests

SITE_URL = 'https://www.markt.de/'
CATEGORY = 'fahrzeuge/autos/'
PARENT_CLASS = 'clsy-c-search__blocks-results'
LI_CLASS = 'clsy-c-result-list-item--wide'
START_PAGE = 4
END_PAGE = 50

url = SITE_URL + CATEGORY

with open('maincar.scv', 'a', encoding='utf-8',newline="") as f:
    for page in range(START_PAGE, END_PAGE):
        webPage = requests.get(url+f'?page={page}')
        soup = BS(webPage.content, 'html.parser')
        allItems = soup.find('div', class_= PARENT_CLASS).findAll('li', class_= LI_CLASS)
        
        ads = []
        
        for item in allItems:
            try:
                ads.append(item.find('h2', class_ = 'clsy-c-result-list-item__title').text.replace(',',' ')) # title
                ads.append(item.find_all('a')[0].get('href')) # link
                location = item.find('div', class_ = 'clsy-c-result-list-item__location').text.replace(',',' ')
                if len(location)>0:
                    ads.append(location)
                else: ads.append('null no location provided')
                price = item.find('div', class_ = 'clsy-c-result-list-item__price-amount').text.replace(',','.').replace('â‚¬','€')
                if len(price)>0: 
                    ads.append(price)
                else:
                    ads.append('null no price provided')
                ads.append([image['data-src'] for image in item.findAll('img')][0]) # img
                file_writer = csv.writer(f)
                file_writer.writerow(ads)
                ads = []
            except:
                print('error in data', item , page)
                ads = []            
        time.sleep(randint(30,90))
        
    f.close()
                
print('\n*****************************done********************************\n')
