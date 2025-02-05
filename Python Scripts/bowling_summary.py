import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Parsing links to get the bowling scorecard

with open("scorecard.csv", "r") as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        url = "https://www.espncricinfo.com" + str(row["Scorecard_link"])
        score_card = requests.get(url)
        soup = BeautifulSoup(score_card.content, 'html.parser')
        try:
            table = soup.find_all("table", class_ = "ds-w-full ds-table ds-table-md ds-table-auto")[0]
            table2 = soup.find_all("table", class_ = "ds-w-full ds-table ds-table-md ds-table-auto")[1]
        except IndexError:
            pass
        
        first_inning_bowl = []
        second_inning_bowl = []

        for row in table.find_all("tr", class_ ="")[1:]:
            cells = [td.text.strip() for td in row.find_all('td')]
            first_inning_bowl.append(cells)
        

        for row in table2.find_all("tr", class_ ="")[1:]:
            cells = [td.text.strip() for td in row.find_all('td')]
            second_inning_bowl.append(cells)
        

        with open('bowling_summary_final.csv', 'a') as csvfile:
            bowler_name = csv.writer(csvfile)
            for row in first_inning_bowl:
                bowler_name.writerow(row)
            for row in second_inning_bowl:
                bowler_name.writerow(row)
        first_inning_bowl.clear()
        second_inning_bowl.clear()








