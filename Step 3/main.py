import random

number = random.randint(0, 100)

userInput = int(input())
# We use an if statement to compare the user's guess with the random number
if userInput > number:
    print("Your guess was too HIGH")
# The elif statement is used when only one outcome should occur
elif userInput < number:
    print("Your guess was too LOW")
