# hangman game- project 3

# sample input:
# Let's Play Hangman!!
# You have only 6 lives so try to guess the word within 6 attempts! Good Luck!!
# ['-', '-', '-', '-', '-']

# Generate a random word from a list

import random
word_list = ['apple', 'buzzy','jazzy','break','chair']
fist_guess = random.choice(word_list)
print(fist_guess)

first_life = '''
           +---+ 
           |   |
           O   |
               |
               |
               |
        ==========
'''
print("Let's Play Hangman!!")
print("You have only 6 lives so try to guess the word within 6 attempts! Good Luck!!")
print("['_', '_', '_', '_', '_']")
second_guess = input("Guess a letter: ")
if second_guess not in fist_guess:
    print(f"You guessed {second_guess} that is not present in the word. So you lose a life.")
    print("['_', '_', '_', '_', '_']")
    print(first_life)
else:
    if second_guess == 'a':
        print("['a', '_', '_', '_', '_']")
        print(first_life)
    elif second_guess == 'p':
        print("['_', 'p', '_', '_', '_']")
        print(first_life)
    elif second_guess == 'l':
        print("['_', '_', '_', 'l', '_']")
        print(first_life)
    elif second_guess == 'e':
        print("['_', '_', '_', '_', 'e']")
        print(first_life)



