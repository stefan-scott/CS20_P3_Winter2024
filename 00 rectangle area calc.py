# Rectangle Area Calculator (title)
# Mr. Scott (name)
# April 11, 2024 (date)
# First look at I/O + data type conversions

# STEP 1 - ask user for width/height
#   *** INPUT ALWAYS GIVES US A STRING ***
#  int()  float()  bool()  str()

width = input("Enter a width: ")
width = float(width)

height = input("Enter a height: ")
height = float(height)

# Calculate Solution and Output to User
area = width * height
#          STR       +  STR       +    STR
print("The area is: " + str(area) + " units squared.")


