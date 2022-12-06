import random

userGuess = input("Enter your guess from 1-100\n")
x = random.randint(1, 100)
print("The number predicted is : ", x)
if userGuess != x:
    print("You failed, would you like to try again? \n Enter Yes or  No")
    answer = input()
    if answer == "Yes":
        print("Okay")
    else:
        print("GoodBye")
else:
    print("You won the guessing game")

