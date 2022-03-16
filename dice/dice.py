# Guess dice

import random

score = 0
for i in range(10):
    dice = random.randint(1,6)
    guess = int(input("Guess dice?"))
    print(f"It was {dice}")
    if guess==dice:
        score+=1


print(f"Your score is {score} ")
