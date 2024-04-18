# Ask the user for their name, store in variable
# Ask for an amount of money, in CAD, store in a var
# Compute the corresponding value in YEN (1:110), store in var
# Print some output, (referencing all 3 variables)

# input() → always gives us a STR
# to convert data:  int()  float() str()  bool()
name = input("Enter your name: ")

amount_cad = input("Amount in CAD? ") #STR
amount_cad = float(amount_cad) #FLOAT

amount_yen = amount_cad * 110

print("Hello, " + name + ".")
print(str(amount_cad) + "CAD = " + str(amount_yen) + " YEN.")
#        STR          +  STR     +    STR          +   STR   

