# Warm-up Number Guesser
# Mr. Scott
# April 15, 2024
# Simple number guessing game

import random

# Choose and store a "hidden number"
hidden_number = random.randint(1,100) #1-100

#Conditional Loop is best here.
user_guess = -1  #placeholder
while user_guess != hidden_number:
    user_guess = input("Enter a number: ") #STR
    user_guess = int(user_guess) #convert str to number

    #check if the number is too high, too low
    if user_guess > hidden_number:
        print("Too high!")
    elif user_guess < hidden_number:
        print("Too low!")

# get out of the loop once the guess is correct
print("You got it!")
    