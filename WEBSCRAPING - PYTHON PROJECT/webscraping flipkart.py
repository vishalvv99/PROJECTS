#webscraping flipkart mobiles under 30k

import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices =[]
Description = []
Reviews = []

for i in range(2,7):
    URL = "https://www.flipkart.com/search?q=5g+mobiles+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    page = requests.get(URL)
    #print(page)

    soup = BeautifulSoup(page.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")

    for i in names:
        name = i.text
        Product_name.append(name)

    #print(Product_name)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)

    #print(Prices)


    desc = box.find_all("ul", class_ = "_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)

    #print(Description)


    reviews = box.find_all("div", class_ = "_3LWZlK")

    for i in reviews:
        name = i.text
        Reviews.append(name)

#print(Reviews)

#to make the dataframe for csv file
df = pd.DataFrame({"Product Name": Product_name,"Prices": Prices, "Description": Description,"Reviews":Reviews})
print(df)
df.to_csv("D:/vishal class/PROJECT/webscraping python/flipkart_mobiles_under_30k.csv")

