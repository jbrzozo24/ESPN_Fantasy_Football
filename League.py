import pandas
import requests



class League(object):
    def __init__(self, leagueID, years=[],swid=None, espn_s2=None):
        self.leagueID=leagueID
        self.player_dict={}
        self.years_dict= self.config(years)
        self.SWID= swid
        self.espn_s2=espn_s2
        
    
    def config(self, years):
        return 0