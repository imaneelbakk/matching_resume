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
# # titles=[]
# # locations=[]=[]
# titles=[]
# contracts=[]
# locations=[]
# levels=[]
# experiences=[]
# requirements=[]
# companies=[]
df = pd.DataFrame(columns=["Title", "Company","Location","Study","Experience","Requirement","Contract"])
for i in range(1, 11):
    int=str(i)
    data=requests.get("https://www.rekrute.com/offres.html?s=3&p="+int+"&o=1&sectorId%5B0%5D=24")
    #create a soup object
    soup=BeautifulSoup(data.content,"lxml")
    #print(soup) #to visualize all the dom of the website
    job_titles=soup.find_all("h2",{"style":"width:90%"})
    for j in range(len(job_titles)):
        links.append(job_titles[j].find("a").attrs["href"])
        print('+link')
for link in links:
    result=requests.get('https://www.rekrute.com'+link)
    src=result.content
    soup=BeautifulSoup(src,'lxml')
    try:
        title=soup.find("h1").text
    except:
        title='none'
    try:
        contract=soup.find("span",{"class":"tagContrat","title":"Poste avec Management"}).text.strip()
    except:
        contract='none'
    try:
        location=soup.find("span",{"id":"address"}).text
    except:
        location='none'
    try:
        level=soup.find('ul',{"class":"featureInfo"}).find_all('li')[2].text.strip()
    except:
        level='none'
    try:
        exp=soup.find('ul',{"class":"featureInfo"}).find_all('li')[0].text
    except:
        exp='none'
    try:
        requirement=soup.find_all('div',{"class":"col-md-12 blc"})[3].text.replace("\n", "").replace("\xa0","").replace("\t", "").replace("Profil recherché :", "").strip()
    except:
        requirement='none'
    try:
        company=soup.find('h4').text.replace("Les dernières offres d’emploi de « ", "").replace(" »", "").replace("?","")
    except:
        company='none'
    df = df.append({"Title":title, "Company":company,"Location":location,"Study":level,"Experience":exp,"Requirement":requirement,"Contract":contract},ignore_index=True)
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
print(len(df))
df.to_csv("./csvFiles/rekrut.csv", index=False)