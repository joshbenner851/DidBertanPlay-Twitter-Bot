import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from time import sleep

#Need to get the gameId programmatically
#LOL nevermind lets just scrape his static profile for each game

def didPlayCurrent():
    try:

        url = "http://www.espn.com/nba/player/_/id/6426/davis-bertans"
        req = urllib.request.Request(url, None, headers={'User-Agent' : 'Mozilla/5.0'})
        html = urllib.request.urlopen(req)
        sleep(10)
        soup = BeautifulSoup(html)

        if(soup == ""):
            print("error with request")

        modContent = soup.findAll("div", {"class": "mod-content"})
        tr = BeautifulSoup(str(modContent[3]))


        recentGame = BeautifulSoup(str(tr.findAll("tr")[1]))
        minutes = recentGame.findAll("td")[3].text
        print(minutes)
        if(int(minutes) > 0):
            return True
        print()
    except Exception as e:
        print(e)
        return e



