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
print("You have",lives, "lives remaining")

userLetter = input("Enter your guess: ")
for letter in keyword: #you guessed right
    if userLetter == letter: #replaces underscore with letter
        print()

    
if userLetter not in usedLetters: #you guessed wrong
    usedLetters += userLetter
    print("You have used ", usedLetters)
elif userLetter in use


while lives < 6:
    print("You have",lives, "lives remaining")
    userLetter = input("Enter your guess: ")
    lives -= 1



if userLetter not in usedLetters:
    usedLetters += userLetter