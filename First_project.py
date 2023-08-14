# Rock/Paper/Scissor
# 0 --> Rock, 1--> Paper, 2--> Scissor
# Rules-01: Rock(0) wins against scissor(2)
# Rule-02: Paper (1) wins against Rock(0)
# Rule-03: Scissor(2) wins against Paper (1)

# 9 possibilities-->  user input (0, 0, 0)  --> computer input(0, 1, 2)
# user input (1, 1, 1)  --> computer input(0, 1, 2)
# user input (2, 2, 2)  --> computer input(0, 1, 2)

# if user input 0 and computer input 0 then match draw *
# if user input 0 and computer input 1 then computer wins *
# if user input 0 and  computer input 2  then user wins----

# if user input 1 and computer input 0 then user wins *
# if user input 1 and computer input 1 then match draw *
# if user input 1 and computer input 2  then computer wins *

# if user input 2 and computer input 0 then computer wins----
# if user input 2 and computer input 1 then user wins
# if user input 2 and computer input 2  then match draw *

# take input from the user  and use it randomly

import random
#user_input = int(input("Enter your choice: Rock(0), Paper(1) or Scissor(2)."))
rock = '''
rock
    -------
---'   (-----)
       (------)
       (------)
       (-----)
----'  (----)
'''

paper = '''
paper
   -------
---'   -----)
       --------)
       --------)
       -------)
---- '  ----)
'''

scissor = '''
scissor
   -------
---'   (-----)
        ----------)
        ----------)
      (-------)
---- ' ( ----)
'''
# game_image = [rock, paper, scissor]
# if user_input >= 0 and user_input <= 2:
#
#     print(f"Your Choice: {game_image[user_input]}")
#     computer_input = random.randint(0, 2)
#
#     print(f"Computer's Choice: {game_image[computer_input]}")
#     if user_input == 0 and computer_input == 2:
#         print("You win.")
#     elif user_input == 2 and computer_input == 0:
#         print("You lose.")
#     elif user_input == computer_input:
#         print("Match draw")
#     elif computer_input > user_input:
#         print("You lose.")
#     elif user_input > computer_input:
#         print("You win.")
# else:
#     print("Invalid input. Please type 0, 1, or 2.")
game_image = [rock, paper, scissor]
user_input = int(input("Enter you choice Rock(0), Paper(1), Scissor(2):"))
print(f"User Choice: {game_image[user_input]}")

if user_input >= 0 and user_input <= 2:
    computer_input = random.randint(0, 2)
    print(f"Computer Choice: {game_image[computer_input]}")
    if user_input == 0 and computer_input == 2:
        print("You win.")
    elif user_input == 2 and computer_input == 0:
        print("You lose.")
    elif user_input == computer_input:
        print("Match Draw")
    elif computer_input > user_input:
        print("computer Win")
    elif user_input > computer_input:
        print("You Win.")
    else:
        print("Invalid input. Please type 0, 1, or 2.")