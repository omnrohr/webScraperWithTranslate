import time
from bs4 import BeautifulSoup as BS
import requests



# theFile = open('D:\webScraber\scaped.csv', 'r')

# for line in theFile:
#     print(line)

item =[]

with open('D:\\webScraber\\forTest.csv', 'r') as f:
    theFile = csv.reader(f)
    contentArray = []
    for line in theFile:
        contentArray.append(line)
    
    # contentArray.pop(0)
    
    links_array = []
    for line in contentArray:
        links_array.append(line[1])
# print(contentArray)
# counter = 0
# for link in links_array:
#     url = links_array[counter]
#     print(url)
#     content = requests.get(url).text
#     print(content)
#     with open("page%s.txt"%counter, 'w', encoding='utf-8') as new_txt_file:
#         new_txt_file.write(content)
#     counter +=1
#     new_txt_file.close()
#     time.sleep(60)
    
        
        
# url = 'https://de.orthostage.com/'
# res = requests.get(url).text
# with open('orhtherstage.txt', 'w',encoding='utf-8') as oursite:
#     oursite.write(res)
# soup = BS(res,'lxml')

# print(type(res))


# url = links_array[0]
# content = BS(requests.get(url), 'lxml')
# content.find_all('div')

# print()


with open('new_scraped_date.csv', 'w', encoding='utf-8') as new_file:
    for i in range(5):
        # append items form scraped file
        item.append(contentArray[i][0]) #title
        item.append(contentArray[i][1]) # link
        # print("content array i 1",contentArray[i][1])
        
        # geting items form scraped page
        with open(f"page{i}.txt", 'r') as testFile:
            content = BS(testFile.read(), 'lxml')
            if (content.find('div', class_ ="clsy-c-expose-details__price-amount")):
                item.append(content.find('div', class_ ="clsy-c-expose-details__price-amount").text.replace('â‚¬',"€"))
            else: item.append("null")
            
            item.append(" >> ".join(i.text for i in content.find('section', class_='clsy-c-expose-attributes').findAll('a')))
                
            theTargetDiv = content.find('div', class_='clsy-contentsection--hor-padding')
            item.append(" ".join(" ".join(i.text for i in theTargetDiv.find_all('p')).split()))
            item.append(contentArray[i][4]) #img link 
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(item)
            item = []
            testFile.close()
