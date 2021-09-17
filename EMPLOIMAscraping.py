import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
from selenium import webdriver
import time
import pandas as pd
from lxml import html
links=[]
dates=[]
df = pd.DataFrame(columns=["Title", "Company","Location","Experience","Studies-level","Domain","Requirements","Contract","Links","Date"])
for i in range(0, 6):
    int=str(i)
    data=requests.get("https://www.emploi.ma/recherche-jobs-maroc/informatique?f%5B0%5D=im_field_offre_metiers%3A31&page="+int)
    soup=BeautifulSoup(data.content,"lxml")
    job_titles=soup.find_all("h5")
    for j in range(len(job_titles)):
        links.append(job_titles[j].find("a").attrs["href"])
        print('+link')
    D=soup.find_all('p',{"class":"job-recruiter"})
    for k in range(len(D)):
        datePure=D[k].text
        datePure=datePure.split('|', 1)[0].strip()
        dates.append(datePure)
date_compteur=0
for link in links:
    result=requests.get('https://www.emploi.ma/'+link)
    src=result.content
    soup=BeautifulSoup(src,'lxml')
    try:
        title=soup.find("h1",{"class":"title"}).text
    except:
        title='null'
    try:
        contract=soup.find("div",{"class":"field field-name-field-offre-contrat-type field-type-taxonomy-term-reference field-label-hidden"}).text.strip()
    except:
        contract='null'
    try:
        location=soup.find("td",{"style":"margin-left: 5px;"}).text
    except:
        location='null'
    try:
        level=soup.find('table',{"class":"job-ad-criteria"}).find_all('tr')[6].find('div',{"class":"field-item even"}).text.strip()
    except:
        level='null'
    try:
        exp=soup.find('div',{"class":"field field-name-field-offre-niveau-experience field-type-taxonomy-term-reference field-label-hidden"}).text.strip().replace("Expérience entre ", "").replace("Débutant ","")
    except:
        exp='null'
    try:
        requirement=soup.find('div',{"class":"content clearfix"}).find_all('ul')[0].text
    except:
        requirement=soup.find('div',{"class":"content clearfix"}).find_all('div')[2].text
    print(requirement)
    try:
        company=soup.find('div',{"class":"company-title"}).text
    except:
        company='null'
    try:
        domain=soup.find('div',{"class":"field field-name-field-offre-secteur field-type-taxonomy-term-reference field-label-hidden"}).text
    except:
        domain='null'
    try:
        date=dates[date_compteur]
        date_compteur+=1
    except:
        date='null'
        date_compteur+=1
    df = df.append({"Title":title, "Company":company,"Location":location,"Experience":exp,"Studies-level":level,"Domain":domain,"Requirements":requirement,"Contract":contract,"Links":'https://www.emploi.ma'+link,"Date":date},ignore_index=True)
    print('+job')
# df.to_csv("./csvFiles/emploima.csv", index=False)
print(len(df))
