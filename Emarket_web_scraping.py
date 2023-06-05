
import pandas as pd
import datetime

from bs4 import BeautifulSoup
import requests

base_url='https://www.noon.com/'

product_links=[]

for x in range(1,65):
    r=requests.get(f'https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page={x}')
    soup=BeautifulSoup(r.content)
    #print(soup)
    spans=soup.find_all('span',{'class':'sc-5e739f1b-0 gEERDr wrapper productContainer'})
    for span in spans:
        links=soup.find_all('a')
        for link in links:
            productlinks=base_url+link['href']
            product_links.append(productlinks)
            print(product_links)
