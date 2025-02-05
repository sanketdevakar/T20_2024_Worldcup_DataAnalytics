import requests
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import csv
import re

url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/squads"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
team_name = []
squad_link = []
for squad in soup.find_all("div", class_ = "ds-flex ds-flex-row ds-space-x-2 ds-items-center"):
    team = squad.find("span").text
    team_name.append(team)
    full_squad = squad.find("a").get("href")
    squad_link.append(full_squad)

age = []
batting_style = []
bowling_style = []
player_name = []
position = []
image =[]

for i in range(len(squad_link)):
    print(team_name[i])
    url2 = "https://www.espncricinfo.com" + str(squad_link[i])
    r2 = requests.get(url2)
    soup = BeautifulSoup(r2.content, "html.parser")
    div1 = soup.find_all("div", class_ = "ds-relative ds-flex ds-flex-row ds-space-x-4 ds-p-3")
    for i in div1:
    
        data = i.find_all("span", class_ = "ds-text-compact-xxs ds-font-bold")
        img_src = i.find("img").get("src")
        image.append(img_src)
        player = i.find_all("a")[1].span.text
        player_name.append(player)
        print(player)
        if len(data) > 2:
            age.append(data[0].text)
            batting_style.append(data[1].text)
            bowling_style.append(data[2].text)
        elif len(data) == 2:
            age.append(data[0].text)
            batting_style.append(data[1].text)
            bowling_style.append("None")
        else:
            age.append(data[0].text)
            batting_style.append("None")
            bowling_style.append("None")


        position.append(i.find("p").text)
  


df = pd.DataFrame({'Player_Name': player_name,  'Age' : age, 'Batting_style': batting_style, 'Position': position, 'Bowling_Style': bowling_style,
                   'Image': image})
df.to_csv('Squad.csv', index=False, encoding='utf-8')
