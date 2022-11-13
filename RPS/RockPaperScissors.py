import random
import sys
import os


moves = ['rock', 'paper', 'scissors']
for option in moves:
    1 < 2
    2 < 3
    3 < 1


    def game():                                
        print("3, 2, 1, SHOOT: ")
        x = input()                             
        if x in moves:
            y = random.choice(moves)            
            print(y)
        else:
            print('Not valid move. Select valid move')
            os.execl(sys.executable, sys.executable, *sys.argv)

        if x > y:
            print("you win")
        elif x == y:
            print("tie")
        else:
            print("you lost")
        print('...')


    def final():
        q = input("play again: Y/N? ")
        if q == 'Y':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif q == "N":
            sys.exit("GAME OVER")
        else:
            print("not valid")
            final()


play = game(), final()


    




