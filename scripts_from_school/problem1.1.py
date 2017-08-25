'''Thomas Whitzer 159005085'''

def magic(n):

    '''takes in a positive number and returns True or False if the the sum of n's divisors (not including n) equal n, meaning it is a Magical Number'''

    a = sum(i for i in range(1,n) if n%i == 0)
    if a == n:
        return True
    return False

def magic_list(num):

    '''creates a list of all magical numbers from 2 to num'''

    return list(filter(magic, range(2,num+1)))