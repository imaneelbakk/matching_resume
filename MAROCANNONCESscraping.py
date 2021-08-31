from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#specify driver path
# DRIVER_PATH = 'C:\webdrivers\chromedriver.exe'
# driver = webdriver.Chrome(executable_path = DRIVER_PATH)
# driver.implicitly_wait(0)



links=[]
title = []
Company=[]
Location=[]
level=[]
domaine = []
contract=[]
requirements=[]
df = pd.DataFrame(columns=["Title", "Company","Location","Studies-level","Domain","Contract"])

for i in range(0,20):
    #driver.get('https://ma.indeed.com/jobs?q=stage%20informatique&l=Maroc&start=' + str(i))
    data = requests.get('https://www.marocannonces.com/maroc/offres-emploi-domaine-informatique-multimedia-internet-b309.html?f_3=Informatique+%2F+Multim%C3%A9dia+%2F+Internet&pge=' + str(i))
    soup = BeautifulSoup(data.text, "lxml")
    job_titles=soup.find_all("div",{"class":"holder"})


    for j in range(len(job_titles)) :
        links.append(job_titles[j].find("a").attrs["href"])

for link in links:


    result = requests.get('https://www.marocannonces.com/'+link)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    try:
        title = soup.find("h1").text
    except:
        title="none"
    try:

        Company = soup.find('ul',class_="extraQuestionName").find_all('li')[3].find_all('a')[0].text.strip()
    except:

        Company = 'none'
    try:

        contract = soup.find('ul', class_="extraQuestionName").find_all('li')[2].find_all('a')[0].text.strip()
    except:

        contract = 'none'
    try:

        Location = soup.find('ul', class_="info-holder").find_all('li')[0].find_all('a')[0].text.strip()
    except:

        Location = 'none'
    try:

        level = soup.find('ul', class_="extraQuestionName").find_all('li')[5].find_all('a')[0].text.strip()
    except:

        level = 'none'
    try:

        domaine = soup.find('ul', class_="extraQuestionName").find_all('li')[1].find_all('a')[0].text.strip()
    except:

        domaine = 'none'
    # try:
    #
    #     requirements = soup.find('div', class_="block").find_all('br').text.strip()
    # except:
    #
    #     requirements = 'none'
    # print(requirements)

    df = df.append({"Title": title, "Company": Company, "Location": Location, "Studies-level": level, "Domain": domaine, "Contract": contract}, ignore_index=True)


df.to_csv("./csvFiles/marocannonces.csv", index=False)