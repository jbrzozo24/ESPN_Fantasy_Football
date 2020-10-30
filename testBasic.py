from League import League  
import os 


def main():
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
