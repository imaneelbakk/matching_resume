#import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
# import selenium
# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
# from time import sleep
# path="C:\webdrivers\chromedriver.exe"
# driver=webdriver.Chrome(path)
links=[]
dates=[]
# # titles=[]
# # locations=[]=[]
# titles=[]
# contracts=[]
# locations=[]
# levels=[]
# experiences=[]
# requirements=[]
# companies=[]
df = pd.DataFrame(columns=["Title", "Company","Location","Experience","Studies-level","Domain","Requirements","Contract","Links","Date"])
for i in range(1, 11):
    int=str(i)
    data=requests.get("https://www.rekrute.com/offres.html?s=3&p="+int+"&o=1&sectorId%5B0%5D=24")
    #create a soup object
    soup=BeautifulSoup(data.content,"lxml")
    #print(soup) #to visualize all the dom of the website
    D=soup.find_all("em",{"class":"date"})
    job_titles=soup.find_all("h2",{"style":"width:90%"})
    for j in range(len(job_titles)):
        links.append(job_titles[j].find("a").attrs["href"])
        print('+link')
    for k in range(len(D)):
        dates.append(D[k].find_all("span")[0].text)
compteur_dates=0
for link in links:
    result=requests.get('https://www.rekrute.com'+link)
    src=result.content
    soup=BeautifulSoup(src,'lxml')
    try:
        title=soup.find("h1").text
    except:
        title='null'
    try:
        contract=soup.find("span",{"class":"tagContrat","title":"Poste avec Management"}).text.strip()
    except:
        contract='null'
    try:
        location=soup.find("span",{"id":"address"}).text
    except:
        location='null'
    try:
        level=soup.find('ul',{"class":"featureInfo"}).find_all('li')[2].text.strip()
    except:
        level='null'
    try:
        exp=soup.find('ul',{"class":"featureInfo"}).find_all('li')[0].text
    except:
        exp='null'
    try:
        requirement=soup.find_all('div',{"class":"col-md-12 blc"})[3].text.replace("\n", "").replace("\xa0","").replace("\t", "").replace("Profil recherché :", "").strip()
    except:
        requirement='null'
    try:
        company=soup.find('h4').text.replace("Les dernières offres d’emploi de « ", "").replace(" »", "").replace("?","")
    except:
        company='null'
    try:
        date=dates[compteur_dates]
        compteur_dates+=1
    except:
        date='null'
        compteur_dates+=1
    df = df.append({"Title":title, "Company":company,"Location":location,"Experience":exp,"Studies-level":level,"Domain":"Informatique","Requirements":requirement,"Contract":contract,"Links":'https://www.rekrute.com'+link,"Date":date},ignore_index=True)
    print('+job')

    # experiences.append(exp)
    # levels.append(level)
    # locations.append(location)
    # contracts.append(contract)
    # titles.append(title)
    # requirements.append(requirement)
    # companies.append(company)

# fileList=[titles,companies,locations,levels,requirements,experiences,contracts]
# export=zip_longest(*fileList)

# with open("/Users/LENOVO/Desktop/StageMoumen/webscraping/webscrapingREKRUT/rekrut.csv","w") as rekrut:
#     wr =csv.writer(rekrut)
#     wr.writerow(["Job Title","company"])
    # wr.writerows(export)

# df.to_csv("./csvFiles/rekrut.csv", index=False)

print(len(df))