# Loop and a Half
# Mr. Scott
# April 17, 2024
# "Forever" Loop, break, continue

while True:  #infinite loop
    choice = input("Stop the loop? [yes/no]") #"YES" , "Yes", "YeS"
    if choice.lower() == "yes":
        confirm = input("Are you sure? [yes/no]")
        if confirm.upper() == "YES":
            break           #Stops the loop at this precise moment
        else:
            continue    # 'restarts' the loop
                        # immediately moves to the next iteration
    print("let's ask again...")