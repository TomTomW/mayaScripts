'''Thomas Whitzer 159005085'''

from decimal import *

class ChangeJar:

    def __init__(self, D = {25: 0, 10: 0, 5: 0, 1:0}):

        coins = [25, 10, 5, 1]
        tempDict = {}
        names = {25:'quarters', 10:'dimes', 5:'nickels', 1:'pennies'}
        
        if D == {25: 0, 10: 0, 5: 0, 1:0}:
            tempDict = D
            self.jar = tempDict
        else:
            for d in coins:
                if d in D:
                    continue
                else:
                    tempDict[d] = 0
            for i in D:
                if i in coins:
                    tempDict[i] = D[i]
                else:
                    print(Exception(i, ':is not a coin'))
        self.jar = tempDict

    def get_change(self, dollar_amt): #returns new change jar and modifies self.
        q = self.jar[25]
        d = self.jar[10]
        n = self.jar[5]
        p = self.jar[1]
        TWOPLACES = Decimal(10) ** -2
        
        #variables for creating a new class at the end of the method
        new_q = q
        new_d = d
        new_n = n
        new_p = p
        
        take_q = 0
        take_d = 0
        take_n = 0
        take_p = 0

        while dollar_amt > 0:
            #checking quarters
            if dollar_amt >= 0.25 and q != 0:
                #print('CHECKING QUARTERS')
                test = int((dollar_amt / 25) * 100)
                if q - test < 0:                   #subtracts the proper number of quaters from dollar_amt
                    old_q = q
                    take_q = q
                    q = 0
                    new_q = q
                    dollar_amt -= (old_q * 25) / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
                else:
                    q = q - test
                    take_q = test
                    new_q = q 
                    dollar_amt -= (test * 25) / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
            #checking dimes
            elif dollar_amt >= 0.10 and d != 0:
                #print('CHECKING DIMES')
                test = int((dollar_amt / 10) * 100)
                if d - test < 0:
                    old_d = d
                    take_d = d
                    d = 0
                    new_d = d
                    dollar_amt -= (old_d * 10) / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
                else:
                    d = d - test
                    take_d = test
                    new_d = d
                    dollar_amt -= (test * 10) / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
            #checking nickels
            elif dollar_amt >= 0.05 and n != 0:
                #print('CHECKING NICKELS')
                test = int((dollar_amt / 5) * 100)
                if n - test < 0:
                    old_n = n
                    take_n = n
                    n = 0
                    new_n = n
                    dollar_amt -= (old_n * 5) / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
                else:
                    n = n - test
                    take_n = test
                    new_n = n
                    dollar_amt -= (test * 5) / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                
            #checking pennies
            elif dollar_amt >= 0.01 and p != 0:
                #print('CHECKING PENNIES')
                test = int(dollar_amt * 100)
                if p - test < 0:
                    old_p = p
                    take_p = p
                    p = 0
                    new_p = p
                    dollar_amt -= old_p / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
                else:
                    p = p - test
                    take_p = test
                    new_p = p
                    dollar_amt -= test / 100
                    dollar_amt = float(Decimal(dollar_amt).quantize(TWOPLACES))
                    
            #if there is not enough change in self.jar
            else:
                return Exception('not enough change in Jar')
        self.jar = ChangeJar({25:new_q, 10:new_d, 5:new_n, 1:new_p})
        return ChangeJar({25: take_q, 10: take_d, 5: take_n, 1: take_p})

    def __getitem__(self, idx):

        if idx in [1, 25, 10, 5]:
            return self.jar[idx]
        if idx < 25 and idx not in [1,5,10,25]:
            return 0
        else:
            raise StopIteration
        
    def insert(self, coin_value, num_coin):

        self.jar[coin_value] = self.jar[coin_value] + num_coin
        return self.jar

    def total_value(self):
        q = self.jar[25]
        d = self.jar[10]
        n = self.jar[5]
        p = self.jar[1]
        TWOPLACES = Decimal(10) ** -2

        qTotal = (25 * q) / 100
        dTotal = (10 * d) / 100
        nTotal = (5 * n) / 100
        pTotal = p / 100
        Totalchange = float(Decimal(qTotal +dTotal + nTotal + pTotal).quantize(TWOPLACES))

        return Totalchange
        
    def __str__(self):

        names = {25:'quarters', 10:'dimes', 5:'nickels', 1:'pennies'}
        q = self.jar[25]
        d = self.jar[10]
        n = self.jar[5]
        p = self.jar[1]

        string = str(q) + ':' + 'quarters' + ',' + ' ' + str(d) + ':' + 'dimes' + ',' + ' ' + str(n) + ':' + 'nickels' + ',' + ' ' + str(p) + ':' + 'pennies'

        return string

    def __repr__(self):

        a = '<' + str(self.jar) + '>'
        return a

    def __add__(self, anotherjar):

        q = self.jar[25] + anotherjar[25]
        d = self.jar[10] + anotherjar[10]
        n = self.jar[5] + anotherjar[5]
        p = self.jar[1] + anotherjar[1]

        return ChangeJar({25:q, 10:d, 5:n, 1:p})

    def __eq__(self, anotherjar):

        if self.total_value() == anotherjar.total_value():
            return True
        else:
            return False

    def __ne__(self, anotherjar):

        if self.total_value() != anotherjar.total_value():
            return True
        else:
            return False
    
