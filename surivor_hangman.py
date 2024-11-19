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

wordBank = ["Council", "Immunity", "Idol","Merge","Blindside","Alliance","Outwit", "Outplay", "Outlast", "Tribal", "Reward", "Challenge", "Immunity","Vote"
, "Jury","Castaway","Buff","Torch","Snuffed","Puzzle","Auction","Camp","Social Game", "Jeff", "Probst","Journey","Parvati", "Cirie"] # 27 items
keyword = random.choice(wordBank)
# chooses keyword before game begins
# 6 drawings = 6 lives

#initial settings
usedLetters = list()
blanks = list()
lives = 6
failedTries = 0

#Display
print("Welcome to Survivor Hangman!")
print("FOR TESTING PURPOSES: the keyword is", keyword)
print(HANGMANPICS[0])
blanks = ["_"]*len(keyword)
print(blanks)
print("You have",lives, "lives remaining")
userLetter = input("Enter your guess: ")
while failedTries < 6:
  print("You have",lives, "lives remaining")
  userLetter = input("Enter your guess: ")
  for index, letter in enumerate(keyword):
    if userLetter == letter: #when you guess right
      blanks[index] = userLetter
      print(blanks)
    else: #you guessed wrong, new hangman appears
      usedLetters += userLetter
      print("You have used ", usedLetters)
      failedTries+=1
      print(HANGMANPICS[failedTries])
      lives -= 1

# for letter in keyword: 
#     if userLetter == letter: #you guessed right, underscore is replaced and printed
#         blank.replace(keyword[letter], userLetter) # the correct section is buggy as hell
#         print(blank)
#         userLetter = input("Enter your guess: ")
#     if userLetter != letter: #you guessed wrong, new hangman appears
#         usedLetters += userLetter
#         print("You have used ", usedLetters)
#         failedTries+=1
#         print(HANGMANPICS[failedTries])
#         lives -= 1
#         print(blank)
#         userLetter = input("Enter your guess: ")
#         if lives == 0:
#             print("The word was ", keyword,". The tribe has spoken")
#             break
# what happens if you win?!