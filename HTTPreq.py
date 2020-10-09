import requests
import pprint as pp
import League

URL = ''
APIurl= ''

SWID = ''
espn_s2 = ''


#Sets the URL to be scraped according to the year
def setURL(year, id):
    #URL = URL + 'https://fantasy.espn.com/football/league/standings?leagueId=143434&seasonId=' +str(year)
    return """https://fantasy.espn.com/apis/v3/games/ffl/seasons/{lgyear}/segments/0/leagues/{lgid}""".format(lgyear=year, lgid= id)  #current season



APIurl= setURL(2020, 143434)
print(APIurl)

page = requests.get(APIurl, cookies = {"swid": SWID,"espn_s2": espn_s2 }) #get the HTML file at this URL

JSON = page.json()

print(JSON)
