import random

number = random.randint(0, 100)

userInput = None  # This is set before the while loop because it is used in the while loop calculation
# A while loop is introduced to repeat all indented lines until the condition is met.
while not userInput == number:
    userInput = int(input())
    if userInput > number:
        print("Your guess was too HIGH")
    elif userInput < number:
        print("Your guess was too LOW")
print("Well done! The number was %d" % number)
