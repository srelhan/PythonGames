import random

player = input('Whats your name? ')
print ('Welcome '+player)
guesscount = 0
number = random.randint(1,20)
print ('The computer is thinking of a number between 1 to 20')
while guesscount < 6:
    guess = int(input(player + ':: your guess '))
    if (guess < number):
        print ('The Guess is too low to match')
    if (guess > number):
        print ('The Guess is too high to match')
    if guess == number:
        print ('Voila Exact Match - YOU WIN')
        break
    guesscount = guesscount + 1
if guess == number:
    print ('The number of guess taken is '+str(guesscount))
if guess == number:
    print ('The random number is '+str(number))

        
