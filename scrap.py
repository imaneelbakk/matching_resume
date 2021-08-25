import requests
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver")

df = pd.DataFrame(columns=["Title", "Location","Company","domain","description","level", "requierements","type_contrat"])

for i in range(0, 500, 10):
    driver.get('https://ma.indeed.com/jobs?q=stage%20informatique&l=Maroc&start=' + str(i))
    stages=[]
    driver.implicitly_wait(4)

    for stage in driver.find_elements_by_id('vjs-desc'):

        soup = BeautifulSoup(job.get_attribute('innerHTML'), 'html.parser')

        try:
            title = soup.find("div", id_="vjs-jobtitle").text.replace("\n", "").strip()

        except:
            title = 'None'

        try:
            location = soup.find(id_="vjs-loc").text
        except:
            location = 'None'

        try:
            company = soup.find(id_="vjs-cn").text.replace("\n", "").strip()
        except:
            company = 'None'

        try:
            domain=soup.find('ul').find_all('li')[1].text

        except:
            domain = 'None'



        try:

            description =soup.find(id_="vjs-desc").text.replace("\n", "").strip()


        except:

            description = "none"


        try:


            level = soup.find('ul').find_all('li')[5].text


        except:

            level = "none"


        try:


            type_contrat = soup.find('ul').find_all('li')[3].text


        except:

            type_contrat = "none"
        try:

            requierements = soup.find('ul').find_all('li')[5].text


        except:

            requierements = "none"

            sum_div = job.find_element_by_xpath('./div[3]')
        try:
            sum_div.click()
        except:
            close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
            close_button.click()
            sum_div.click()

        df = df.append({'Title': Title, 'Location': Location, "Company": Company, "domain": domain,
                         "description": description,"level":level,"requierements":requierements,"type_contrat":type_contrat}, ignore_index=True)

        print("Got these many results:", df.shape)


df.to_csv("data.csv", index=False)