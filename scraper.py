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
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.implicitly_wait(30)

driver.get('https://indeed.com')
quoi = driver.find_element_by_xpath('//*[@id="text-input-what"]')
q_key="stage informatique"
quoi.send_keys([q_key])
o_key="maroc"
ou = driver.find_element_by_xpath('//*[@id="text-input-where"]')
ou.send_keys([o_key])


try:
    initial_search_button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
    initial_search_button.click()
except:

    close_popup = driver.find_element_by_id("popover-close-link")
    close_popup.click()
links=[]
title = []
Company=[]
Location=[]
Study=[]
Domaine = []
contract=[]
for i in range(0,10,1):
    # driver.get('https://ma.indeed.com/jobs?q=stage%20informatique&l=Maroc&start=' + str(i))
    data = requests.get('https://ma.indeed.com/emplois?q=stage+informatique&l=Maroc&start=' + str(i))
    soup = BeautifulSoup(data.content, "lxml")
    job_card=soup.find_all("a",{"target":"_blank"})


    driver.implicitly_wait(10)

    # for j in range(len(job_card)):
    #
    #     links.append(job_card[j].find("a").attrs["href"])

        #for job in job_card:




    #
    #     for link in links:
    #         driver.get(link)
    #         print(link)
    #
    #         try:
    #
    #             jt =soup.find_all("div", id_="vjs-jobtitle").text.replace("\n", "").strip()
    #             title.append(jt)
    #         except:
    #             title.append('none')
    #
    #         try:
    #             jc =driver.find_element_by_xpath(' /html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[4]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/ul/li[3]').text.strip()
    #             contract.append(jc)
    #         except:
    #             contract.append('none')
    #
    #         try:
    #             jl =driver.find_element_by_xpath('//*[@id="vjs-loc"]').text.strip()
    #             Location.append(jl)
    #         except:
    #
    #             Location.append('none')
    #
    #         try:
    #             JS= driver.find_element_by_xpath('//*[@id="vjs-desc"]/div[2]/div[2]/ul/li[6]').text.strip()
    #             Study.append(JS)
    #         except:
    #             Study.append("none")
    #         try:
    #             JC=driver.find_element_by_xpath('//*[@id="vjs-desc"]/div[2]/div[2]/ul/li[4]').text.strip()
    #             Company.append(JC)
    #         except:
    #             Company.append("none")
    #
    #         try:
    #
    #             JD=driver.find_element_by_xpath('//*[@id="vjs-desc"]/div[2]/div[2]/ul/li[1]').text.strip()
    #             Domaine.append()
    #         except:
    #             Domaine.append("none")
    #     df_da = pd.DataFrame()
    #     df_da['Title'] = title
    #     #df_da['Company'] = Company
    #     #df_da['Location'] = Location
    #     #df_da['Domaine'] = Domaine
    #     #df_da['contract'] = contract
print(job_card)
#         print("Got these many results:", df_da.shape)
# df_da.to_csv("data2.csv")
































