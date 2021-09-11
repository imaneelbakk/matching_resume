import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
from selenium import webdriver
import time
import pandas as pd
links=[]
df = pd.DataFrame(columns=["Title", "Company","Location","Experience","Studies-level","Domain","Requirements","Contract","Links"])
for i in range(0, 5):
    int=str(i)
    data=requests.get("https://www.emploi.ma/recherche-jobs-maroc/informatique?f%5B0%5D=im_field_offre_metiers%3A31&page="+int)
    soup=BeautifulSoup(data.content,"lxml")
    job_titles=soup.find_all("h5")
    for j in range(len(job_titles)):
        links.append(job_titles[j].find("a").attrs["href"])
        print('+link')

for link in links:
    result=requests.get('https://www.emploi.ma/'+link)
    src=result.content
    soup=BeautifulSoup(src,'lxml')
    try:
        title=soup.find("h1",{"class":"title"}).text
    except:
        title='none'
    try:
        contract=soup.find("div",{"class":"field field-name-field-offre-contrat-type field-type-taxonomy-term-reference field-label-hidden"}).text.strip()
    except:
        contract='none'
    try:
        location=soup.find("td",{"style":"margin-left: 5px;"}).text
    except:
        location='none'
    try:
        level=soup.find('table',{"class":"job-ad-criteria"}).find_all('tr')[6].find('div',{"class":"field-item even"}).text.strip()
    except:
        level='none'
    try:
        exp=soup.find('div',{"class":"field field-name-field-offre-niveau-experience field-type-taxonomy-term-reference field-label-hidden"}).text.strip().replace("Expérience entre ", "").replace("Débutant ","")
    except:
        exp='none'
    # try:
    #     requirement=soup.find('ul').find_all('li')[5].text.strip()
    # except:
    #     requirement='none'
    # print(requirement)
    try:
        company=soup.find('div',{"class":"company-title"}).text
    except:
        company='none'
    try:
        domain=soup.find('div',{"class":"field field-name-field-offre-secteur field-type-taxonomy-term-reference field-label-hidden"}).text
    except:
        domain='none'
    df = df.append({"Title":title, "Company":company,"Location":location,"Experience":exp,"Studies-level":level,"Domain":domain,"Requirements":'none',"Contract":contract,"Links":'https://www.emploi.ma/'+link},ignore_index=True)
    print('+job')

print(len(df))
