import random

from random import randint

def generator(): # function to generate a random number on each execution
    return randint(1,10)

def rand_guess(): # function to return true or false based on user lucky draw
    random_number = generator() # call to generator()
    guess_left = 3 # define the number of guesses the user gets
    flag = 0 # define flag variable to check the win condition
    while guess_left > 0:
        guess = int(input("Pick your number to enter the lucky draw\n"))
        if guess == random_number:
            flag = 1 # Set flag as 1 if user guesses correctly. Then break loop
            break
        else:
            print("Wrong Guess!")
            guess_left -= 1 # decrease number of remaining guesses by 1
    if flag == 1: #if win condition is satisifed, then rand_guess returns true
        return True
    else:
        return False
# Driver code
if __name__ == '__main':
    print("Congrats!! You Win")
else:
    print("Sorry, You Lost!")
