import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

player_name = []
runs = []
dismissal = []
balls_faced = []
fours = []
sixes = []
strikerate = []   
mins = []

# Parsing links to get the batting scorecard

with open("scorecard.csv", "r") as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        url = "https://www.espncricinfo.com" + str(row["Scorecard_link"])
        score_card = requests.get(url)
        soup = BeautifulSoup(score_card.content,'html.parser')
        
        try:
            table = soup.find_all("table", class_ = "ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table")[0]
            table2 = soup.find_all("table", class_ = "ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table")[1]
        except IndexError:
            pass

        first_inning = []
        second_inning = []


        for row in table.find_all("tr", class_ =""):
            cells = [td.text.strip() for td in row.find_all('td')]
            first_inning.append(cells)
        try:
            for i in range(len(first_inning)-2):
                player_name.append(first_inning[i][0])
                dismissal.append(first_inning[i][1])
                runs.append(first_inning[i][2])
                balls_faced.append(first_inning[i][3])
                fours.append(first_inning[i][5])
                sixes.append(first_inning[i][6])
                strikerate.append(first_inning[i][7])
        except IndexError:
            pass
            

        for row in table2.find_all("tr", class_ =""):
            cells = [td.text.strip() for td in row.find_all('td')]
            second_inning.append(cells)
        
        try:
            for i in range(len(second_inning)-2):
                player_name.append(first_inning[i][0])
                dismissal.append(first_inning[i][1])
                runs.append(first_inning[i][2])
                balls_faced.append(first_inning[i][3])
                fours.append(first_inning[i][5])
                sixes.append(first_inning[i][6])
                strikerate.append(first_inning[i][7])
        except IndexError:
            pass

        
        first_inning.clear()
        second_inning.clear()

df = pd.DataFrame({'Player': pd.Series(player_name), 'Dismissal': pd.Series(dismissal), 'Runs' : pd.Series(runs), 'Balls': pd.Series(balls_faced), '4s': pd.Series(fours), '6s': pd.Series(sixes),
                   'Strikerate': pd.Series(strikerate) })

df.to_csv('Main1.csv', index=False, encoding='utf-8')     






    
    
    
    

    



    

