import random
HANGMANPICS = ['''

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

def getRandomWord(wordlist):
    return wordlist[random.randint(0, len(wordlist)-1)]

def playAgain():
    print('Do you want to play again ? (yes/no)')
    return input().lower().startswith('yes')

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretword):
    print (HANGMANPICS[len(missedLetters)])
    print ()

    print ('Missed Letters', end=' ')
    for letter in missedLetters:
        print (letter, end='|')

    blanks = '_' * len(secretword)
    print ()
    for i in range(len(secretword)):
        if secretword[i] in correctLetters:
            blanks = blanks[:i]+secretword[i]+blanks[i+1:]
    for letter in blanks:
        print(letter, end='|')
                   
def getGuess(alreadyUsed):
    while True:
        print ('Guess a letter')
        guess = input()
        if guess in alreadyUsed:
            print ('Try Again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Try Again')
        else:
            return guess
                   
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()           
print ("H A N G M A N")
secretword = getRandomWord(words)
#print (secretword)
gameisDone = False
missedLetters = ''
correctLetters = ''

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretword)
    guess = getGuess(missedLetters+correctLetters)

    if guess in secretword:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range (len(secretword)):
            if secretword[i] not in correctLetters:
                foundAllLetters =  False
                break
        if foundAllLetters:
            print ('You have won')
            gameisDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretword)
            print ('You have lost')
            print ('The Secret Word is ' + secretword)
            gameisDone = True
        
    if gameisDone:
        if playAgain():
            print ('Its Yes')
            gameisDone = False
            missedLetters = ''
            correctLetters = ''
            gameisDone = False
            secretword = getRandomWord(words)
        else:
            print ('Its not Yes')
            break
    





 

