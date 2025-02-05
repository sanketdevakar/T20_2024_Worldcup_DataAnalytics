import requests
from bs4 import BeautifulSoup
import html5lib
import pandas as pd

url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/match-schedule-fixtures-and-results"

r = requests.get(url)

with open("file.html", "w") as f:
   f.write(r.text)

soup = BeautifulSoup(r.content, 'html.parser')

list1 =[]
for scorecard in soup.find_all("a", attrs={'class': "ds-no-tap-higlight"}):
   if "icc-men-s-t20-world-cup-2024" in str(scorecard.get("href")):

      list1.append(scorecard.get("href"))

# Storing scorecard links into csv file 

df = pd.DataFrame({'Scorecard_link' : list1})
df.to_csv('scorecard.csv', index=False, encoding='utf-8')

