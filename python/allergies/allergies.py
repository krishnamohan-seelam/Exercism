from enum import IntFlag

class Allergy(IntFlag):
    EGGS = 1
    PEANUTS = 2
    SHELLFISH = 4
    STRAWBERRIES = 8
    TOMATOES = 16
    CHOCOLATE = 32
    POLLEN = 64
    CATS =128


class Allergies(object):

    def __init__(self, score):
        self.score =score

    def is_allergic_to(self, item):
        return  item in self.lst

    @property
    def lst(self):
        binary_scores = reversed(bin(self.score)[2:])
        return [ allergy.name.lower() for binary_score,allergy  in zip(binary_scores,Allergy) if binary_score =='1']