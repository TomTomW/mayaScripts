'''Thomas Whitzer 159005085'''

def is_leap(yr):

    '''
    takes in yr: returns if it is a leapyear
    '''

    if  0 == yr % 400:
        return (True)
    elif 0 == yr % 4 and yr % 100 != 0:
        return (True)
    else:
        return (False)

def monthdays(yr, mon):

    '''
    takes in yr, mon: returns number of days in month
    '''
    largeMon = [1,3,5,7,8,10,12]
    smallMon = [4,6,9,11]
    feb = 2
    if is_leap(yr) == True and mon== 2:
        return 29
    elif mon in smallMon:
        return 30
    elif mon in largeMon:
        return 31
    else:
        return 28



class Date:

    min_year = 1800
    dow_jan1 = 'Wednesday'

    def __init__(self, month = 1, day = 1, year = min_year):
        self.min_year = 1800

        if month >= 1 and month <= 12:
            self.__month = month
        else:
            print(Exception('Month not between 1 and 12 inclusive.'))
        if day <= monthdays(year, month): 
            self.__day = day
        else:
            print(Exception('Day does not occur in month'))
        if year >= self.min_year:
            self.__year = year
        else:
            print(Exception('Year must be 1800 or after'))

            
    def month(self):
        return self.__month

    def day(self):
        return self.__day

    def year(self):
        return self.__year

    def year_is_leap(self):
        
        '''
        checks if self.year() is a leap year
        '''
        if  0 == self.year() % 400:
            return (True)
        elif 0 == self.year() % 4 and self.year() % 100 != 0:
            return (True)
        else:
            return (False)

    def monthdays(self):

        '''
        takes in self: returns number of days in month
       '''
        largeMon = [1,3,5,7,8,10,12]
        smallMon = [4,6,9,11]
        feb = 2
        if self.year_is_leap() == True and self.month() == 2:
            return 29
        elif self.month() in smallMon:
            return 30
        elif self.month() in largeMon:
            return 31
        else:
            return 28

    def yeardays(self):

        '''
        takes in self: returns number of days in year
        '''

        if self.year_is_leap() == True:
            return 366
        else:
            return 365

    def daycount(self):
        from_month = 1
        from_day = 1
        from_year = self.min_year
        counter = 0
        
        
        for i in range(from_year, self.__year + 1):
            if self.month() == from_month and self.day() == from_day and self.year() == from_year:
                counter = 1
                return counter
            elif i != self.__year:  # checks that i to make sure not to add too many days
                d = Date(self.month(), 1, i) #creates new Date class to run yeardays()
                counter += d.yeardays()
            else:
                for m in range(1, self.__month +1):
                    if m != self.__month:
                        d  = Date(m, 1, self.year()) #creates new Date class to run monthdays()
                        counter += d.monthdays()
                    else:
                        counter += self.day()
        return counter
        

    def day_of_week(self):   

        '''
        day of the week of self
        '''

        d = self.daycount() - 1
        day = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        m = d % 7
        
        return day[m]

    def nextday(self):

        '''
        takes in self: returns class of the next day
        '''

        a = self.day() + 1

        if self.month() == 12 and a > self.monthdays(): #if 12/31/year return 1/1/year+1
            month = 1
            day = 1
            year = self.year() + 1
            #print(str(month) + '/' + str(day) + '/' + str(year))
            return Date(month, day, year)
        elif a > self.monthdays():                     #if at the end of month increase month + 1
            month = self.month() + 1
            day = 1
            year = self.year()
            #print(str(month) + '/' + str(day) + '/' + str(year))
            return Date(month, day, year)
        else:
            month = self.month()
            day = a
            year = self.year()
            #print(str(month) + '/' + str(day) + '/' + str(year))
            return Date(month, day, year)

    def prevday(self):

        '''
        takes in self: retruns class of the previous day
        '''

        a = self.day() - 1

        if self.month() == 1 and a == 0:  #if 1/1/year return 12/31/year-1
            month = 12
            day = 31
            year = self.year() - 1
            if year < self.min_year:
                return Exception('Date occurs before the year 1800')
            else:
                checker = Date(month, day, year)
                #return str(month) + '/' + str(day) + '/' + str(year)
        elif a == 0:                      #if at the beginning of month decreases month - 1
            month = self.month() - 1
            year = self.year()
            d = Date(month, 1, year)
            day = d.monthdays()
            checker = Date(month, day, year)
            #return str(month) + '/' + str(day) + '/' + str(year)
        else:
            month = self.month()
            day = a
            year = self.year()
            checker = Date(month, day, year)
            #return str(month) + '/' + str(day) + '/' + str(year)
        return Date(month, day, year)


    def __add__(self, n):

        x = self
        counter = 0

        while counter < n:
            x = x.nextday()
            counter += 1
        print(str(x.month()) + '/' + str(x.day()) + '/' + str(x.year()))
        
    def __sub__(self, n):

        x = self
        counter = 0

        while counter < n:
            x = x.prevday()
            counter += 1
        print(str(x.month()) + '/' + str(x.day()) + '/' + str(x.year()))


    def __lt__(self, otherclass):

        a = self.daycount()
        b = otherclass.daycount()

        if a < b:
            return True
        else:
            return False

    def __le__(self, otherclass):

        a = self.daycount()
        b = otherclass.daycount()

        if a <= b:
            return True
        else:
            return False

    def __gt__(self, otherclass):

        a = self.daycount()
        b = otherclass.daycount()

        if a > b:
            return True
        else:
            return False

    def __ge__(self, otherclass):

        a = self.daycount()
        b = otherclass.daycount()

        if a >= b:
            return True
        else:
            return False

    def __eq__(self, otherclass):

        a = self.daycount()
        b = otherclass.daycount()

        if a == b:
            return True
        else:
            return False


    def __ne__(self, otherclass):

        a = self.daycount()
        b = otherclass.daycount()

        if a != b:
            return True
        else:
            return False
        

    def __str__(self):

        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        
        return months[self.month()] + ' ' + str(self.day()) + ',' + ' ' + str(self.year())

    def __repr__(self):
        
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        
        a = '<' + months[self.month()] + ' ' + str(self.day()) + ',' + ' ' + str(self.year()) + '>'
        
        return a
        
