import requests
from bs4 import BeautifulSoup
import pandas as pd

import csv
f = open('path', 'w')
writer = csv.writer(f)

headers = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

product_links=[]
for x in range(0,26):
    link=f'https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/product-reviews/B09G9D8KRQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}'
    product_links.append(link)
    #print(product_links)

#print(len(product_links))

for links in product_links:
    r=requests.get(links, headers=headers)
    soup=BeautifulSoup(r.content,'lxml')
    reviews_title=soup.find('div',class_="a-section a-spacing-none review-views celwidget")
    for title in reviews_title:
        Title=title.find('a',class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold")
        try:
            writer.writerow(Title)
            print(Title.text.strip())
        except:
            print("")
f.close()
