import random

HHANGMAN_PICT = ["""
    +----+
         |
         |
         |
        ===
    """,
                 """ 
                 +----+
                     |
                      |
                      |
                     ===
                 """,
                 """
                 +----+
                 0    |
                 |    |
                      |
                     ===
                 """,
                 r"""
                 +----+
                 0    |    
                /|    |
                      |
                     ===
                 """,
                 r"""
                 +----+
                 0    |   
                /|\   |
                      |
                     ===
                 """,
                 r"""            
                 +----+
                 0    |   
                /|\   |
                /     |
                     ===
                 """,
                 r"""
                 +----+
                 0    |   
                /|\   |
                / \   |
                     === 
                 """

                 ]

words = 'ayi peleng wir fil donuz qartal piwik it sican qunduz inek qoyun '.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HHANGMAN_PICT[len(missedLetters)])
    print()

    print('Sehf herfler->', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    print('Gizli soz')

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuests(alradyGuessed):
    while True:
        print("Herfi yazin: ")
        guess = input(': ')
        guess = guess.lower()

        if len(guess) != 1:
            print("Zehmet olmasa 1 herf girin!")
        elif guess in alradyGuessed:
            print("Siz bu herfi yazmisiniz!")
        elif guess not in 'abcdefgfhxijkqlmnoprstuvwyz':
            print("Zehmet olmasa herf yazin")
        else:
            return guess


def playAgain():
    print("Yeniden oynamaq isterdinizmi? 'he yoxsa yox'")
    return input().lower().startswith('h')


print('VESELICA')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)

gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuests(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('*************************************')
            print('Beli Gizli soz - "' + secretWord + '"! Siz tapdiniz !')

            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HHANGMAN_PICT) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Siz butun wansinizi istifade etdiniz!\nTapilmayan herf sayi:->' + str(
                len(missedLetters)) + ' herf' + 'tapilan herf sayi-> ' + str(
                len(correctLetters)) + '.Tapilmaqda olan gizli soz--> "' + secretWord + '".')

            gameIsDone = True

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
