'''Thomas Whitzer 159005085'''

import random

def roll_dice():

    '''rolls two dice and sums them'''

    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    return die_one + die_two


def play_one_game():

    '''Plays a single game of craps without betting. Rolls the dice with rules.'''

    roll = roll_dice()
    win = [7,11]
    lose = [2,3,12]
    roll_again = [4,5,6,8,9,10]

    if roll in win:
        print('You rolled', roll,  '\nYou win!\n')
        return 1
    elif roll in lose:
        print ('You rolled', roll, '\nSorry, you lose!\n')
        return 0
    elif roll in roll_again:
        print('You rolled', roll, "\nYour point is" , roll,'\n')
        c = 'continue'
        while c == 'continue':
            again = roll_dice()
            if again == roll:
                c = 'done'
                print('You rolled', roll,  '\nYou win!\n')
                return 1
            elif again == 7:
                print('You rolled 7',  '\nSorry, you lose!\n')
                return 0
            else:
                print('You rolled', again)


def craps():

    '''This function plays a game of craps'''

    bank = 1000

    print('\nYour initial bank balance is $1000.')
    while bank > 0:
        bet = int(input('What is your wager? $'))
        if bet <= bank:
            print("Okay, let's play.\n")
            game = play_one_game()
            if game == 1:
                bank = bank + bet
                print('Your new bank balance is $',bank,'\n')
                play_again = input('Would you like to play again? [y/ n] ')
                if play_again == 'y':
                    pass
                elif play_again == 'n':
                    break
            else:
                bank = bank - bet
                print ('Your new bank balance is $', bank)
                play_again = input('would you like to play again? [y/ n] ')
                if bank == 0:
                    print("Sorry you're broke!")
                elif play_again == 'y':
                   pass
                elif play_again == 'n':
                   break
        else:
            print('You cannot wager more than', bank ,'.' , ' Re-enter wager:')


print('____!!!WELCOME TO THE CRAPS TABLE!!!____\n')
craps()