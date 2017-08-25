'''Thomas Whitzer 159005085'''

from problem3a import *


def symmetric_difference(c1, c2):

    '''
    returns a new Container with all items that occure in both c1 and c2
    '''

    a = c1.items()
    b = c2.items()
    NewContainer = Container()
    n = NewContainer.items()

    for i in a:
        if i in b:
            continue
        else:
            if i in n:
                continue
            else:
                n.append(i)
    for i in b:
        if i in a:
            continue
        else:
            if i in n:
                n.remove(i)
            else:
                n.append(i)
    NewContainer = Container(n)
    return NewContainer

def subcontainer(c1, c2):

    '''
    returns True if c1 is a sub-container of c2 and False otherwise
    '''
    
    a = c1.items()
    b = c2.items()

    for i in a:
        if i in b and c1.count(i) <= c2.count(i) and len(a) <= len(b):
            return True
        else:
            return False

def remove_repeats(C):

    '''
    returns C without repeating elements
    '''
     
    a = C.items()
    l = []

    for i in a:
        if i in l:
            continue
        else:
            l.append(i)
    C = Container(l)    #Does not return C modified... it should... works otherwise
    print(C)
    return  C


def similar(A, B):

    '''
    returns True if Containers have same elements regaurdless of repeats and False otherwise
    '''

    a = A.items()
    b = B.items()

    for i in a:
        if i in b:
            continue
        else:
            return False
    for i in b:
        if i in a:
            continue
        else:
            return False
    return True

I = Container([1, 2, "abc", 2, [4]])
P = Container([3, 2, 4, "abcd", [4], "xy"])

K = Container([1, 2, 2, 3, 4, 'abc'])
L = Container([1, 2, 2, 3, 4, 'abc', 6, 7])

A = Container([1, 1, 2, 2, 3, 3, 4, 4,])
B = Container([1, 2, 3, 4])

