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
    def __init__(self, leagueID, yearlist=[],swid=None, espn_s2=None):
        self.leagueID=leagueID
        self.player_dict={}
        self.years= self.configYears(yearlist)
        self.SWID= swid
        self.espn_s2= espn_s2
        self.dumpPath= self.configPath() #Create a path to dump files

        try:
            self.cookieFile= open(str(self.leagueID)+"-Cookies.txt", "r")
            if self.cookieFile.readlines() == []:
                self.cookieFile.close()
                self.configCookies(str(self.leagueID)+"-Cookies.txt")
            else:
                self.cookieFile.close()
                self.cookieFile = open(str(self.leagueID)+"-Cookies.txt", "r")
                self.SWID = self.cookieFile.readline()
                self.SWID = self.SWID[:-1]
                self.espn_s2 = self.cookieFile.readline()
                self.cookieFile.close()
        except:
            self.configNewCookies()



    #Configure a Cookies File that already exists, but has no/incorrect data in it  
    def configCookies(self, filename):
        self.cookieFile= open(filename, "w+")
        self.SWID=input("Provide your SWID key as a string (include {}):")
        self.espn_s2=input("Provide your espn_s2 cookie as a string:")
        self.cookieFile.write(self.SWID+"\n")
        self.cookieFile.write(self.espn_s2)
        self.cookieFile.close()

    #Configure a New Cookies File
    def configNewCookies(self):
        filename= os.path.join(self.dumpPath, str(self.leagueID)+"-Cookies.txt")
        self.configCookies(filename)
        # self.cookieFile= open(name, "w+")
        # self.SWID= input("Provide your SWID key as a string (include {}):")
        # self.espn_s2= input("Provide your espn_s2 cookie as a string:")
        # self.cookieFile.write(self.SWID+"\n")
        # self.cookieFile.write(self.espn_s2)
        # self.cookieFile.close()
        

    #Returns a path to save generated files
    def configPath(self): 
        return os.getcwd()

    #Returns a dictionary of years and the associated links with them
    def configYears(self, yearList):
        yeardict= {}
        for year in yearList:
            if year != 2020: 
                yeardict.update({year: "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/"+str(self.leagueID)+"?seasonId="+str(year)})
            else:
                yeardict.update({year: "https://fantasy.espn.com/apis/v3/games/ffl/seasons/"+str(year)+"/segments/0/leagues/"+str(self.leagueID)})
        return yeardict

    #Returns the contents of the mStandings param page
    def getmStandings(self, year):
        url= self.years.get(year) + "?view=mStandings"
        r= requests.get(url, cookies = {"swid": self.SWID,"espn_s2": self.espn_s2 }).json() 
        # print(r)
        return r
