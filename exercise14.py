# Head/Tail- 0 means Heads and 1 means Tails
# a virtual Coin Toss Program in which we will generate a random number and based on that it will tell "Heads or Tails"

import random
side = random.randint(0, 1)
print(side)

if side == 1:
    print("Heads")
else:
    print("Tails")