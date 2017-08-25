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

def yeardays(yr):

    '''
    takes in yr: returns number of days in year
    '''

    if is_leap(yr) == True:
        return 366
    else:
        return 365

def wkday_on_first(yr, mon):

    '''
    given yr and mon: returns day of the week of the 1st of the month
    '''

    number_of_days_in_year = []
    days_to_year = []
    days_of_the_week = {0: 'Tuesday', 1: 'Wednesday', 2: 'Thursday', 3: 'Friday',
    4: 'Saturday', 5: 'Sunday', 6: 'Monday'}

    for p in range(1, mon):
        number_of_days_in_year.append(monthdays(yr, p))
    days_in_yrmonth = sum(number_of_days_in_year)

    for i in range(1754, yr):
        days_to_year.append(yeardays(i))
    days_inbetween = sum(days_to_year)
    days = (days_inbetween+days_in_yrmonth) % 7

    return days_of_the_week[days]


def print_calendar(yr, mon):
    '''
    Doc string
    '''

    months = {1: 'January', 2: ' February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
     8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    weekdays = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    day_of_week = wkday_on_first(yr, mon)
    l = ['Sunday', 'Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday']

    if mon < 1 or mon > 12:
        mon = int(input('Please chose a number between 1 and 12 '))
        print_calendar(yr, mon)
    elif yr <1754:
        yr = int(input('Please type a year greater than or equal to 1754 '))
        print_calendar(yr, mon)
    else:
        print(str(yr).center(30))
        print(months[mon].center(30), '\n')
        print(' '.join(weekdays).center(30))


        j = l.index(day_of_week)
        print(' '.center(5), end = '')
        for i in range(j):                 
            print(' '.rjust(2), end = ' ') 
        
        day_counter = 1
        while day_counter <= monthdays(yr, mon):
            for i in range(6):
                if i == 0:
                    '''top row'''
                    for e in range(7-j):
                        print(str(day_counter).rjust(2), end = ' ') 
                        day_counter += 1
                    print('\n', ' '.center(3), end = '')
                elif i == 5:
                    '''end line'''
                    for e in range(7):
                        if day_counter <= monthdays(yr, mon):
                            print(str(day_counter).rjust(3), end = '')
                            day_counter += 1
                        else:
                            break
                    print('\n', ' '.center(3), end = '')
                else:
                    '''middle row'''
                    for e in range(7):
                        if day_counter <= monthdays(yr, mon):
                            print(str(day_counter).rjust(3), end = '')
                            day_counter += 1
                        else:
                            break
                    print('\n', ' '.center(3), end = '')
        

    





