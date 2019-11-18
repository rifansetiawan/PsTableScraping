import os
from selenium import webdriver
import requests
from os.path import abspath
from os import path
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import csv


#DRIVER = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
DRIVER = 'chromedriver'
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")

#path di bawah ini C:/Users/BN001166774/AppData/Local/Google/Chrome/User Data/Default/ dapat di cek "chrome://version/" 	
chrome_options.add_argument("user-data-dir=C:/Users/BN001166774/AppData/Local/Google/Chrome/User Data/Default/") # Path to your chrome profile or you can open chrome and type: "chrome://version/" on URL

url = 'https://pasardana.id/bond/ADMF03CCN2'

driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 7)

all_html = driver.page_source



###----------ini udah dapet head table sama isi nya, tinggal dirapiin lagi
soup = BeautifulSoup(all_html,"html.parser")
#containers = soup.findAll("tr", {"class": "ng-scope"})
#headers = soup.findAll("table", attrs={"class":"table table-hover stock-table table-bordered table-float-reflow floatThead-table"})
table = soup.findAll("table", attrs={"class":"table"})

datasets=[]
n = 0
for row in soup.findAll("tr")[1:]:
    isinya = [td.get_text() for td in row.findAll("td")]
    datasets.append(isinya)

#print(headers)
print(*datasets, sep = "\n")

#write datasets (table) ke dalam file
with open("listfile.txt", 'w') as filehandle:
    filehandle.writelines("%s\n" % table for table in datasets)



























#----------cara lain open chrome (hanya refrensi)
# chrome_driver_exe_path = abspath("C:/Python37/chromedriver.exe")  # download from https://chromedriver.chromium.org/downloads
# assert path.exists(chrome_driver_exe_path), 'chromedriver.exe not found!'
# web = webdriver.Chrome(executable_path=chrome_driver_exe_path, chrome_options=chrome_options)

# web.get("https://pasardana.id")
