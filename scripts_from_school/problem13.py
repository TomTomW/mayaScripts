'''Thomas Whitzer 159005085'''


def replace_element(L, oldel, newel):

    '''
    Takes in list: iterates through list and replaces oldel with newel
    '''

    if len(L) <= 1:
        if L[0] == oldel:
            L[0] = newel
            return L
        return L
    elif L[0] == oldel:
        L[0] = newel
        return L[:1] + replace_element(L[1:], oldel, newel)
    else:
        return L[:1] + replace_element(L[1:], oldel, newel)


def inverse_pair(L):

    '''
    iterates through list of number looking for a pair of numbers that equal 0
    '''
    
    if len(L) <= 1:
        return False
    elif L[0] + L[-1] == 0:
        return True
    else:
        return inverse_pair(L[1:]) or inverse_pair(L[:-1])


def occurrences(astr, substr):

    '''
    iterates through astr counting the number of times substr occurs
    '''
    
    n = len(substr)
    
    if len(astr) == 0:
        return 0
    else:
        return (astr[0:n] == substr) + occurrences(astr[1:], substr)

    
