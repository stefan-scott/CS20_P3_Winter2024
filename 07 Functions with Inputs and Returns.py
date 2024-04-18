# Functions with Inputs/Returns
# Mr. Scott
# April 18, 2024
# A look at functions and information passing

def add_three(num1, num2, num3):
    # take in three numbers, result is the sum of all
    # num1, num2, num3:  integer values
    return num1 + num2 + num3   # return sends some data
                                #back to replace the function call

result = add_three(2,3,4)  # store return value in a variable
print(add_three(3,5,7))    # print out the return value