import requests
from bs4 import BeautifulSoup


product_links='https://www.w3schools.com/html/html_tables.asp'
link=requests.get(product_links)
print(link)
soup=BeautifulSoup(link.content,'lxml')

#print(soup)

table_data=soup.find('div', class_='w3-white w3-padding notranslate w3-padding-16')

print(len(table_data))
print(table_data)
