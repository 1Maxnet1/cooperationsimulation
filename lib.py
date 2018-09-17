#imports the needed libraries
import numpy as np
from collections import Counter

def playersguess(enemies): #needs an integer of the amount of the enemies
    a = np.arange(101)#creates a list with the integers from 0 to 100
    probability = [#contains a statistc distribution of the result of the guessing game
            0.0952681963865762,
            0.0540917257983409,
            0.0305623140336350,
            0.0361178695891907,
            0.0204585760363785,
            0.0210889722277769,
            0.0191977836535818,
            0.0303873160509029,
            0.0193553827014314,
            0.0232953588976712,
            0.0245561512804679,
            0.0262897408068134,
            0.0197428136940616,
            0.0227525177328559,
            0.0229349240382375,
            0.0205636420682782,
            0.0167331096552674,
            0.0300487699481148,
            0.0169155159606488,
            0.0121729520207305,
            0.0169155159606488,
            0.0131761867003286,
            0.0481981973335714,
            0.0181011569456285,
            0.0102576858142251,
            0.0129025772422564,
            0.0098928732034622,
            0.0160946875864321,
            0.0145442339906896,
            0.0091632479819363,
            0.0090720448292455,
            0.0051503092635439,
            0.0091632479819363,
            0.0382570536902812,
            0.0140882182272360,
            0.0097104668980807,
            0.0055151218743068,
            0.0126289677841842,
            0.0059711376377605,
            0.0041470745839458,
            0.0041470745839458,
            0.0034174493624199,
            0.0118588078281291,
            0.0032451767406707,
            0.0081220119887170,
            0.0058419331714486,
            0.0034351833087764,
            0.0034351833087764,
            0.0031818412179688,
            0.0019784662866327,
            0.0088187027384379,
            0.0051452424217277,
            0.0018517952412289,
            0.0019151307639308,
            0.0029918346498631,
            0.0028334958431084,
            0.0030973938543663,
            0.0028862754453599,
            0.0031501734566179,
            0.0008806505597998,
            0.0004969545565109,
            0.0004969545565109,
            0.0007223117530450,
            0.0024112590250957,
            0.0047335615241654,
            0.0018834630025798,
            0.0054196963534360,
            0.0072142028299898,
            0.0018834630025798,
            0.0017251241958251,
            0.0004969545565109,
            0.0004969545565109,
            0.0004969545565109,
            0.0019362426048314,
            0.0018834630025798,
            0.0018306834003283,
            0.0004969545565109,
            0.0035724102746305,
            0.0026751570363536,
            0.0004969545565109,
            0.0004969545565109,
            0.0006167525485418,
            0.0014084465823156,
            0.0013028873778124,
            0.0005111933440387,
            0.0004969545565109,
            0.0004969545565109,
            0.0025168182295989,
            0.0009862097643029,
            0.0007223117530450,
            0.0004969545565109,
            0.0004969545565109,
            0.0004969545565109,
            0.0009334301620513,
            0.0004969545565109,
            0.0004969545565109,
            0.0004969545565109,
            0.0005111933440387,
            0.0009334301620513,
            0.0004969545565109,
            0.0155006003834883
        ]
    return np.random.choice(a,size=enemies,p=probability).tolist() #returns a list of the length of the amount of enemies with guessed numbers
# Tests whether the function playersguess does what it should do
#guess = []
#for i in range(1000):
#    guess.extend(playersguess(10))
#cnt = Counter(guess)
#for i in range(101):
#    print(str(i) + ' : ' + str(cnt[i]))


def addownguess(enemylist, ownguess):
    enemylist[len(enemylist):] = [ownguess] #needs a list of the guess of the enemies and adds the own guess to this list at the end
    return enemylist # returns a list of all guesses, where your guess is at the end


def findwinnumber(guesses): #needs a full list of guesses
    winnumber = sum(guesses) / len(guesses) * 2 / 3
    return winnumber # returns the analytic number which would win


def closestguess(guesses, winnumber): #needs a full list of guesses and the number which would win the game
    minimumdistancetowinnumber = 100
    winnerspositions = []
    for i in range(len(guesses)):
        differencetowinnumber = abs(guesses[i] - winnumber)
        if differencetowinnumber < float(minimumdistancetowinnumber):
            minimumdistancetowinnumber = differencetowinnumber
            winnerspositions = [] # need to delete previous winners, as we found one that is closer to the winnumber
            winnerspositions[len(winnerspositions):] = [i]
        elif differencetowinnumber == minimumdistancetowinnumber:
            winnerspositions[len(winnerspositions):] = [i]
        else:
            pass
    #print(winnerspositions)
    return winnerspositions #returns a list of the position of the winners of the handed over


def calculateprize(winnerspostions):#needs a list of the winner's positions
    prize = 100 / len(winnerspostions)
    return prize # returns the prize which each winner gets