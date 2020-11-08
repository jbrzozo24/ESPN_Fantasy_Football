from League import League
import os
import sys
import getopt


#===================================================================================
#The main file for running the League Module. 
#   This file is intended to allow for custom command line arguments to personalize 
#   the excel results to display team-specific data, win probability, historical data
#   etc. 
#
#   Arguments:
#       -p: Player to display specific team data for
#       -h: help
#       -y: the year you want to see data for
#
#   Long Arguments:
#       --player: Player to display specific team data for
#       --year: the year you want to see data for
#
#===================================================================================


def main(argv,leagueID):
    league= League(leagueID,[2020]) #Create this League object

    try:
        opts, args = getopt.getopt(argv,"hp:y:",["player=","year="])
    except getopt.GetoptError:
        print("\nInvalid Argument!")
        print ('main.py -p <"firstname lastname">, -y <year>; use "-h" for more help\n')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('\n main.py Arguments: \n\n -p <"firstname lastname"> : This field gives an overview of the team specified by player. Must be a string \n\n -y <year> : Gives an overview of this season in the given league, must be a valid season for this league\n\n')
        elif opt in ('-p', '--player'):
            assert type(arg) == str
            league.dashPscript(arg) #Call the script for player specific data
        elif opt in ('-y', '--year'):
            assert type(arg) == int

    #General script
    league.writeScoreArray(2020)
            




#If running as a script
if __name__=='__main__':
    main(sys.argv[2:],sys.argv[1])