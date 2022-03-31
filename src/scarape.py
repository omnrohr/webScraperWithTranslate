import requests
from bs4 import BeautifulSoup as BS

# url = 'https://de.orthostage.com/'
# req = requests.get(url)
# reqText = req.text
# reqContent = req.content

# with open('reqText.txt', 'w', encoding='utf-8') as fileWriter:
#     fileWriter.write(reqText)
#     fileWriter.close()
 
# # contenet can not be convert to txt or encode to utf   
# # even with beautifulsoup oject it is not able to convert
# soup = BS(reqContent, 'html.parser')
# with open('contentText.txt', 'w', encoding='utf-8') as file2writer:
#     file2writer.write(soup.decode(pretty_print=True))
#     file2writer.close()
    
# soup = BS(req.content, 'html.parser')
# print(soup.decode(pretty_print=True))
# print(type(soup.decode(pretty_print=True)))

with open('contentText.txt', 'r') as readContent:
    webcontent = readContent.read()
    # web content is a str

readContent.close()
#convert the webcontent to beautiful soup object
soup = BS(webcontent, 'html.parser')
#success
section = soup.find('section', class_ = "beautypress-pagefeed-section")
allRows = section.find_all('div',class_='beautypress-welcome-content-group')
print(len(allRows),  type(allRows))

