# ESPN_Fantasy_Football ![Build Status](https://travis-ci.com/jbrzozo24/ESPN_Fantasy_Football.svg?branch=main)
This repository formats ESPN FF information into excel spreadsheets.
For this repository to work, you must install the following dependencies using:

pip install openpyxl
pip install requests
pip install pandas
pip install 

Currently, there is not support for argument based customization of the excel spreadsheet, 
but there are plans to create such features.

Shortly, you will be able to run this code using 
python League.py <leagueId> 
You will be asked to provide your espn SWID and espn_s2 cookie
If your league is public, enter {} for SWID and nothing for espn_s2
If your league is private, you will need to find these cookies from whatever browser you have saved 
your login, and enter them. (This can be found relatively easily using chrome by going to the top right 
three dots and clicking settings, cookies, findin the list of all cookies and expanding the list for
ESPN.com).
