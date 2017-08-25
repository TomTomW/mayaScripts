'''Thomas Whitzer 159005085'''


def pig_latin_word(word):

    '''takes in a word and returns the pig-latin version'''

    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if word[0] in vowels:
        return word+'way'
    else:
        return word[1:]  + word[0] + 'ay'


def pig_latin_sentence(eng_sentence):

    '''takes in an english sentence and returns a pig-latin version'''

    sentList = eng_sentence.split()
    final = ['In Pig Latin:']
    Punc = ['.',',','?','!']
    for i in sentList:
        p = len(i)
        if i[p-1:] in Punc:
            final.append(pig_latin_word(i[:p-1])+i[p-1:])
        else:
                final.append(pig_latin_word(i))
    return '  '.join(final)

def question(answer):

    '''this function prompts a question for continuing to translate'''

    while answer is 'y':
       quest = input('Enter the English sentence into the translator: ')
       print(pig_latin_sentence(quest))
       answer = input('Do antoher? [y/n] ')



quest = input('Enter the English sentence into the translator: ')
print(pig_latin_sentence(quest))
answer = input('Do antoher? [y/n] ')
question(answer)