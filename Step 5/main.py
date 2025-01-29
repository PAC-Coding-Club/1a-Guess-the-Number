import random

# We tell the user how out game works before they make their first guess
print("Im thinking of a number between 0-100, "
      "try guess it and ill let you know if your guess was too low or too high.")

number = random.randint(0, 100)

userInput = None

while not userInput == number:
    userInput = int(input())
    if userInput > number:
        print("Your guess was too HIGH")
    elif userInput < number:
        print("Your guess was too LOW")
print("Well done! The number was %d" % number)
