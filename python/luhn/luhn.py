import re
class Luhn(object):

    VALID_PATTERN = re.compile(r'^\d(\s|\d)+(\s|\d)*$')

    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):

        if not isinstance(self.card_num,str):
            return ValueError("Only strings are allowed")

        if len(self.card_num) <=1 :
            return False
        
        if not self.VALID_PATTERN.match(self.card_num):
            return False

        self.card_num = self.card_num.replace(' ','')
        result =  sum([int(el)*2 -9  
                       if int(el)*2> 9 else int(el)*2  
                       for el in self.card_num[-2::-2]
                       ] +
                      [int(el) for el in self.card_num[-1::-2]
                       ])
        return True if (result % 10 ==0)  else False