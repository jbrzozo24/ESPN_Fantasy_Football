"""
The Player Class.
    Describes a player
    Attributes:
        firstname: The First Name of the Player
        lastname:  The Last Name of the Player
        longID:    The longID of the Player
        displayname: The username of the Player
        teamID:    The ID of the team this player owns
        scores:    A dictionary with keys as years and values are arrays with scores each week


"""
class Player(object):
    def __init__(self, firstname, lastname, longID, displayname=""):
        self.firstname=firstname
        self.lastname=lastname
        self.longID=longID
        self.displayname= displayname
        #Initialize these with stubs
        self.teamID=''
        self.scores={}
        self.phyID=''
        self.wins=None
        self.ties=None
        self.losses=None
        self.ptsFor=None
        self.ptsAgainst=None

    

    #===========================================================================
    # Setters
    #===========================================================================
    def setteamID(self, id):
        self.teamID=id

    def setscores(self, year, array):
        self.scores.update({year: array})


    def setphyID(self, id):
        self.phyID=id

    #Returns the physicalID of this player
    def translate(self):
        return self.phyID
