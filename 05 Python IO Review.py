#Python Input/Output Review


# OUTPUT (lvl 1) - printing one piece of data
print(99)       #print number
print("hello")  #print string literal
text = "CS20"
print(text)     #print variable (str)

# OUTPUT (lvl 2) - printing multiple strings at once
print("hello" + text)  # STR+STR → join/concatenation
print("hello" , text)  # printing with , → prints 2 or more items with space

# OUTPUT (lvl 3) - printing mixed types
num = 45
#          STR       + INT
print("best number:" + str(num))
print("best number:" , num)

# INPUT - reading in values and storing in a variable
number_one = input("Enter a number: ") #STR
number_one = float(number_one) #FLOAT

number_two = float(input("Enter a number: "))

# MATH - calculate an exponent
result = number_one**number_two
print(number_one , "**" , number_two , "=" , result)



