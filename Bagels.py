import random
def getSecretNum(numDigits):
    secretNum = ''
    while (len(secretNum)!= numDigits):
        randomNum = random.randint(0,9)
        if str(randomNum) not in secretNum:
            secretNum += str(randomNum)
    return secretNum
def getClues(guess,secretNum):
    clues=[]
    for digit in range(len(secretNum)):
        if guess[digit] == secretNum[digit]:
            clues.append('Fermi')
        elif guess[digit] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)
        

def playAgain():
    print ('Play Again ? (yes/no)', end=' ')
    return input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

#print (getSecretNum(NUMDIGITS))
while True:
    print ('You are in while loop')
    secretNum = getSecretNum(NUMDIGITS)
    #print ('Secret Number is' + secretNum)
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses=1
    while numGuesses <= MAXGUESS:
          guess = ''
          #print ('u r here in first while')
          while len(guess)!= NUMDIGITS or not guess.isdigit():
              print ('Enter Guess : %s'%(guess),end=' ')
              guess = input()
              #print (len(guess))
              #print (guess.isdigit())
          clue = getClues(guess, secretNum)
          print(clue)
          numGuesses += 1
          
          if guess == secretNum:
              print ('Guessed it right')
              break
          if numGuesses > MAXGUESS:
              print ('Exceeded Guesses, Secret number is %s'%(secretNum))
          
    if not playAgain():
        break
