from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
time.sleep(10)
soup = BeautifulSoup(page.text,"html.parser")
starTable = soup.find('table')
tempList = []
tablerows = starTable.find_all("tr")

for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

starname = []
distance = []
mass = []
radius = []
lum = []

for i in range(1 , len(tempList)):
    starname.append(tempList[i][1])
    distance.append(tempList[i][3])
    mass.append(tempList[i][5])
    radius.append(tempList[i][6])
    lum.append(tempList[i][7])

df2 = pd.DataFrame(list(zip(starname,distance,mass,radius,lum)),columns = ['name','distance','mass','radius','luminosity'])
df2.to_csv("stars.csv")








            
