# Try-Except Demo
# Trying to gracefully handle program errors

#          0   1       2
my_list = [88, 44, "Twenty Two"]

while True:
    try:
        index = int(input("Enter an index:")) #int() with text → ValueError
        item = my_list[index] #index out of range → IndexError
        print("Number:" + item) #can't join str+int → TypeError
        break  # if we reach this line, there were no problems
               # so break loop and carry on with rest of program
    except ValueError:
        print("Value Error")
    except IndexError:
        print("Index Error")
    except TypeError:
        print("Type Error")
    except:
        print("Generic Error")

        
