from bs4 import BeautifulSoup
import requests
import pandas as pd

ProductName = []
Prices = []
Description = []

for i in range(2, 8):
    url = "https://www.flipkart.com/search?q=phones+under+20k&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&as-pos=1&as-type=RECENT&suggestionId=phones+under+20k%7CMobiles&requestId=a632970e-051b-446e-851a-9c777a78d676&as-backfill=on&page=" + str(
        i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extracting product names
    names = soup.find_all("div", class_="_4rR01T")
    for a in names:
        name = a.text
        ProductName.append(name)
        

    # Extracting prices
    prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    for a in prices:
        price = a.text
        Prices.append(price)

    # Extracting descriptions
    descriptions = soup.find_all("ul", class_="_1xgFaf")
    for a in descriptions:
        desc = a.text
        Description.append(desc)

df = pd.DataFrame({"ProductName": ProductName, "Prices": Prices, "Description": Description})
df.to_csv("ProductInfo.csv", index=False)
