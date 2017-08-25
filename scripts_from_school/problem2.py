'''Thomas Whitzer 159005085'''


from problem1 import *



def weekend_dates(m, y):

    number_ofdays = Date(m, 1, y)
    number_ofdays = number_ofdays.monthdays()
    weekend_days =[]

    for d in range(1, number_ofdays+1):
        if Date(m, d, y).day_of_week() in ['Saturday', 'Sunday']:
            print(Date(m, d, y), '', '(',Date(m, d, y).day_of_week(),')')


def first_mondays(y):

    for i in range(1, 13):
        for d in range(1,8):
            if Date(i, d, y).day_of_week() in ['Monday']:
                print(Date(i, d, y))


def interval_schedule(start_date, stop_date, interval):
    a = start_date
    b = stop_date
    helper = start_date
    L = []

    L.append(start_date)
    while helper <= stop_date:
        for i in range(1, interval + 1):
            if i == interval and helper.nextday() < stop_date:
                helper = helper.nextday()
                L.append(helper)
            else:
                helper = helper.nextday()
    for x in L:
        print(x, '\n')
    return L
            
