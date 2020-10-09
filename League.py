import pandas
import requests
import datetime 
import os


"""
The League Class.
    This class describes the league in question
    Attributes:
        leagueID: the ID of this league
        player_dict: A dictionary of players in this league
            Keys: Player name (string) Value: The Player object (sub-class of league)
        years[]: a list of the years this league has been active
        swid: the swid cookie of the user in this league            #used for logging in purposes
        espn_s2: the espn_s2 cookie of the user in this league      #used for logging in purposes
        dumpPath: the path that will be used to dump the cookies file

"""
class League(object):
    def __init__(self, leagueID, years=[],swid=None, espn_s2=None):
        self.leagueID=leagueID
        self.player_dict={}
        self.years_dict= self.config(years)
        self.SWID= swid
        self.espn_s2= espn_s2

        self.dumpPath= self.configPath() #Create a path to dump files

        try:
            self.cookieFile= open(str(self.leagueID)+"-Cookies.txt", "r")
            if self.cookieFile.readlines == []:
                raise Exception()
            self.cookieFile.close()
        except:
            name= os.path.join(self.dumpPath, str(self.leagueID)+"-Cookies.txt")
            self.cookieFile= open(name, "w+")
            self.SWID= "{some string}" #input("Provide your SWID key as a string:")
            self.espn_s2="{some other string}" #input("Provide your espn_s2 cookie as a string:")


        
    def config(self, years):
        return 0

    #Returns a path to save generated files
    def configPath(self): 
        curPath=os.getcwd()
        i=curPath.rfind("\\") #get the last index where the '\' character in encountered
        if i != -1:
            newPath=curPath[:i]
        else:
            newPath=curPath 
        #return newPath 
        return curPath

