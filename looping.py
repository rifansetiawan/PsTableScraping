import os
from selenium import webdriver
import requests
from os.path import abspath
from os import path
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time


#DRIVER = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
DRIVER = 'chromedriver'
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")

#path di bawah ini C:/Users/BN001166774/AppData/Local/Google/Chrome/User Data/Default/ dapat di cek "chrome://version/"     
chrome_options.add_argument("user-data-dir=C:/Users/BN001166774/AppData/Local/Google/Chrome/User Data/Default/") # Path to your chrome profile or you can open chrome and type: "chrome://version/" on URL

url = 'https://pasardana.id/bond/ADMF03CCN2'

driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)

with open('LINKS.csv') as example_file:
    example_reader = csv.reader(example_file)
    for row in example_reader:
        driver.get(row[0])
        name = row[0][26:]
        time.sleep(5)
        # do whatever...
        all_html = driver.page_source
        soup = BeautifulSoup(all_html,"html.parser")
        table = soup.findAll("div", attrs={"class":"tab-pane fade active in"})
        datasets=[]
        n = 0
        for row in soup.findAll("tr")[1:]:
            isinya = [td.get_text().replace(",", "") for td in row.findAll("td")]
            for word in isinya:
                if word.endswith("Outright"):
                    datasets.append(isinya)
        print(*datasets, sep = "\n")
        company = "History_Transaction.csv"
        space = " , , , , , , \n"
        
        
        headers = "Tanggal,High,Low,Last,Value,WAP,Deskripsi \n"
        f = open(company, "a")
        # lines = example_file.readlines()
        # lines[0] = lines[0][26:]
        f.write(space)
        f.write(name + "\n")
        f.write(headers)
        f.close()
        with open(company, 'a') as filehandle:
            filehandle.writelines("%s\n" % table for table in datasets)

        # if (datasets != []):
        #   break

    # driver.close()