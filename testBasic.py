from League import League  
import os 
import sys

class MY_STD_IN( object ):
    def __init__(self, response_list):
        self.std_in_list = response_list
        self.std_in_length = len(response_list)
        self.index = 0

    def readline(self):
        value = self.std_in_list[self.index]      
        print value
        if self.index < self.std_in_length -1:
            self.index += 1
        else:
            self.index = 0

        return value

def main():
    predSTDIN=[ '{}\r', '\r']
    sys.stdin=MY_STD_IN(predSTDIN)
    l= League(164, [2019,2020])
    l.makeScoreArray(2020)
    assert 'katie kosciolek' in l.player_array
    assert 'jordan crump' in l.player_array
    assert 'tim hughes' in l.player_array
    assert 'david gass' in l.player_array
    assert 'cody chaffins' in l.player_array
    assert 'austin mcafee' in l.player_array
    assert 'james zorn' in l.player_array
    assert 'timothy graham' in l.player_array
    assert 'bobby crutchfield' in l.player_array 
    assert 'john gleason' in l.player_array



#If executing this as a script, run this code
if __name__ == '__main__':
    main()
