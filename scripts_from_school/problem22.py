'''Thomas Whitzer 159005085'''

import string




def freq_distribution(infile, distfile):
    '''
    takes in a file and returns the words and their frequency in alphabetical
    order
    '''
    target = open(distfile, 'w')
    word_count = freq_dictionary(infile)
    for k, v in sorted(word_count.items()):
        print(k.ljust(20), ' '.ljust(3),  str(v).ljust(8),'\n')
        i = k.ljust(20) + ' '.ljust(3) + str(v).ljust(8)
        target.write(i)
        target.write('\n')
    target.close()


def ordered_freq_distribution(infile, ordered_distfile):
    '''
    takes in file and returns words in decreasing freq to least with alphabetical sub order
    '''
    J = []
    word_count = freq_dictionary(infile)
    target = open(ordered_distfile, 'w')
    
    for k, v in word_count.items():
        J.append((k, v))
        J = sorted(J, key= lambda J: J[0])
        J = sorted(J, key= lambda J: J[1], reverse=True)
        
    for k, v in J:
        print(k.ljust(20), ' '.ljust(3), str(v).ljust(8),'\n')
        i = k.ljust(20) + ' '.ljust(3) + str(v).ljust(8)
        target.write(i)
        target.write('\n')
    target.close()




def freq_dictionary(infile):

    '''
    takes in file: returns dictionary of words in file and their frequency
    '''


    file = open(infile, 'r')
    read = file.read()

    D = {}

    for char in string.punctuation:
        read = read.replace(char, ' ')
    r = read.split()
    for i in r:
        p = len(i)
        if i[p-1] in string.punctuation:
            if i[:p-1].lower() in D:
                D[i.lower()] += 1
            else:
                D[i[:p-1].lower()] = 1
        else:
            if i.lower() in D:
                D[i.lower()] += 1
            else:
                D[i.lower()] = 1

    file.close()
    return D

