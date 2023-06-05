from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver=webdriver.Chrome("D:/pythonProject/pythonProject/Python/chromedriver.exe")

Name=[]
Designation=[]
Contact_Details=[]
Address=[]

driver.get("https://www.mca.gov.in/content/mca/global/en/contact-us/official-liquidators.html")

content=driver.page_source
soup=BeautifulSoup(content)
names=soup.findAll('tr', class_="view table.value dark.theme diff.designation")
for data in names:
    Name_element=data.find("td", col="Name")
    Designation_element=data.find("td", col="Designation")
    Contact_element=data.find("td", col="Contact_Details")
    Address_element=data.find("td", col="Addredd")
    
    print(Name_element.text)
    print(Designation_element.text)
    print(Contact_element.text, end="\n")
    print(Address_element.text.strip(), end="\n"*2)

    Name.append(Name_element.text)
    Designation.append(Designation_element.text)
    Contact_Details.append(Contact_element.text)
    Address.append(Address_element.text)
    
