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

wordBank = ["Council", "Hidden Immunity Idol","Merge","Blindside","Alliance","Outwit", "Outplay", "Outlast", "Tribal", "Reward", "Challenge", "Immunity Challenge","Vote Split"
, "Jury","Castaway","Buff","Torch Snuffed","Rice Rationing","Puzzle Master","Survivor Auction","Camp Life","Social Game", "Jeff", "Probst","Journey","Parvati", "Cirie"] # 27 items

keyword = random.choice(wordBank)
# chooses keyword before game begins
usedLetters = list()
# 6 drawings = 6 lives
print("Welcome to Survivor Hangman!")
print(HANGMANPICS[0])
blank = len(keyword)*"_ "
print(blank) # prints corresponding underscore for every letter
lives = 6
failedTries = 0
print("You have",lives, "lives remaining")

userLetter = input("Enter your guess: ")
for letter in keyword: 
    if userLetter == letter: #you guessed right, underscore is replaced and printed
        blank.replace(keyword[letter], userLetter)
        print(blank)
        userLetter = input("Enter your guess: ")
    if userLetter != letter: #you guessed wrong, new hangman appears
        usedLetters += userLetter
        print("You have used ", usedLetters)
        failedTries+=1
        print(HANGMANPICS[failedTries])
        lives -= 1
        userLetter = input("Enter your guess: ")
        if lives == 0:
            print("The word was ", keyword,". The tribe has spoken")
            break
# what happens if you win?!