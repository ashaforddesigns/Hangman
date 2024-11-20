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

wordBank = ["fiji", "cbs", "council", "immunity", "idol", "merge", "blindside", "alliance", "outwit", "outplay", "outlast", "tribal", "reward", "challenge", "vote", "jury", "castaway", "buff", "torch", "snuffed", "puzzle", "auction", "camp", "social game", "jeff", "probst", "journey", "parvati", "cirie"] 
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
blankDisplay = " ".join(blanks)
print(blankDisplay)
print("You have",lives, "lives remaining")



while "_" in blankDisplay and lives > 0: # WHILE <-- (this) AND (this) are true...the game continues...
      userLetter = input("Enter your guess: ")
      
      # when you guess wrong
      if userLetter not in keyword:
            usedLetters += userLetter
            print("You have used ", usedLetters)
            failedTries+=1
            print(HANGMANPICS[failedTries])
            lives -= 1
            print("You have",lives, "lives remaining")

      # when you guess right
      for index, letter in enumerate(keyword):
            if userLetter == letter: 
                  blanks[index] = userLetter
                  blankDisplay = " ".join(blanks)
      print(blankDisplay)
             
# outcomes
if "_" not in blankDisplay: #that means you won
      print("Congrats! You are the Sole Survivor!")
else: #you lost and you get the sad outcome
      print("The word was", keyword,". Sorry, the tribe has spoken.")
  
      
      