from cgitb import reset
from multiprocessing.dummy import Array
import time
from unittest import result
from bs4 import BeautifulSoup as BS
import requests
import csv






SCRAPED_FILE_LINK = 'D:\\webScraber\\source.csv'
TARGETED_TO_SAVE_FILE_PATH = 'new_scraped_date.csv'
START_LINE_TO_SCRAPE = 11
END_LINE_TO_SCRAPE = 10

item =[]

with open(SCRAPED_FILE_LINK, 'r', encoding='utf-8') as f:
    theFile = csv.reader(f)
    contentArray = []
    for line in theFile:
        contentArray.append(line)
    # contentArray.pop(0)
    
    links_array = []
    for line in contentArray:
        result = [i for i in line if i.startswith('https')][0]
        links_array.append(result)

with open(TARGETED_TO_SAVE_FILE_PATH, 'w',newline='', encoding='utf-8') as savedExcel:
    for i in range(START_LINE_TO_SCRAPE, len(links_array)):
        try:
            fullPage = BS(requests.get(links_array[i]).content, 'lxml')
            item.append(contentArray[i][0]) #title
            item.append(contentArray[i][1]) # link
            if (fullPage.find('div', class_ ="clsy-c-expose-details__price-amount")):
                    item.append(fullPage.find('div', class_ ="clsy-c-expose-details__price-amount").text.replace('â‚¬','€'))
            else: item.append("null")
            if fullPage.find('section', class_='clsy-c-expose-attributes').findAll('a'):
                item.append(" >> ".join(i.text for i in fullPage.find('section', class_='clsy-c-expose-attributes').findAll('a')))
            else: item.append('null')
            theTargetDiv = fullPage.find('div', class_='clsy-contentsection--hor-padding')
            if theTargetDiv.find_all('p'):
                item.append(" ".join(" ".join(i.text for i in theTargetDiv.find_all('p')).split()))
            else: item.append('null')
            if contentArray[i][4]:
                item.append(contentArray[i][4]) #img link 
            else: item.append('null')
            csv_writer = csv.writer(savedExcel)
            csv_writer.writerow(item)
            item = []
            time.sleep(30)
        except: 
            print('error in files')
            csv_writer = csv.writer(savedExcel)
            csv_writer.writerow(item)
            item = []
            time.sleep(10)
            
    f.close()
    savedExcel.close()