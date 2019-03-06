# Score categories
# Change the values as you see fit
from collections import Counter

YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):

    if not len(dice)== 5 :
        return 0

    value_counter = Counter(dice)

    if category ==YACHT :
        return 50 if len(set(dice)) ==1 else 0

    elif category in (ONES ,TWOS,THREES,FOURS,FIVES,SIXES):
        return  dice.count(category) *category

    elif category == FULL_HOUSE:
        if set(value_counter.values()) ==set([2,3]):
            return sum(dice)

    elif category ==FOUR_OF_A_KIND:
        key,value  =value_counter.most_common(1)[0]
        return  4* key if value >= 4 else 0

    elif category  == LITTLE_STRAIGHT:
        return 30 if set(dice) == set([1,2,3,4,5]) else 0

    elif category  == BIG_STRAIGHT:
        return 30 if set(dice) == set([2,3,4,5,6]) else 0
    
    elif  category == CHOICE:
        return sum(dice)

    return 0 
            
    

