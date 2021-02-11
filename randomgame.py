from random import randint
import sys


number = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = int(input(f'guess a number between {sys.argv[1]}-{sys.argv[2]}: '))

        if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
            if guess == number:
                print(f'That\'s right! My number was {number}')        
                break
            else:
                print('Try again!')
                continue
    except ValueError:
        print('please enter a number 1-10')
        continue

