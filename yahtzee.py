import random
import collections
import itertools

'''
Simulate Yahtzee rolls to see percentage of each category
'''

def check_dice(dice, score):
    '''
    dice: list of 5 dice numbers
    score: defaultdict to keep track of scoring categories
    '''
    long_straights = [(1,2,3,4,5),(2,3,4,5,6)]
    short_straights = [(1,2,3,4),(2,3,4,5),(3,4,5,6)]
    rigoles = [(1,6),(2,5),(3,4)]
    
    for long_straight in long_straights:
        if set(long_straight) == set(dice):
            score['long straight'] += 1
            score['short straight'] += 1
            return 
    for short_straight in short_straights:
        if set(short_straight).issubset(dice):
            score['short straight'] += 1
            return 
    if len(set(dice)) == 1:
        score['yahtzee'] += 1
        score['full house'] += 1
        score['four of a kind'] += 1
        return 
    ###
    # check for full house, 4 of a kind, and rigole
    # these can all occur when set length is 2
    ###

score = collections.defaultdict(int)
combos = [d for d in itertools.product((1,2,3,4,5,6), repeat=5)]
for dice in combos:
    check_dice(dice, score)
for k,v in score.items():
    print(k, v, v/len(combos)*100)
    
