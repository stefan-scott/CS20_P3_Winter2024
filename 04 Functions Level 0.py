# Fortune Teller Machine

# Functions "level 0" (no inputs, no outputs)
# Useful for reuse of code, for organization

def fortune_one():
    # prints out a fortune for the user
    print("Today is your lucky day!!")

def fortune_two():
    # prints out another fortune for the user
    print("Don't step on the cracks...")

def fortune_three():
    # prints out a fortune for the user
    print("Your lucky number is 113")
    
# MAIN CODE STARTS HERE...
# Use random numbers to select which of the three
# fortunes to display.
import random
roll = random.randint(0,2)  #0,  1,  2
if roll == 0:
    fortune_one()
elif roll == 1:
    fortune_two()
else:  #2
    fortune_three()

#Another comment for the next section...