# Micro:bop:it Starter
# Mr. Scott
# June 12, 2024

import microbit, time, random

# Set up data for the program
choices = ["A", "S"] #also needs B, L(←) R(→)
target_action = random.choice(choices)

# Set up time data...
start_time = time.time()
time_to_choose = 2 #specify number of seconds for the user to make an action

while True:
    elapsed_time = time.time() - start_time
    
    # show user the "Target Action" on microbit display
    if target_action == "S":
        microbit.display.show(microbit.Image.SKULL)
    elif target_action == "L":
        pass  # replace with drawing the left arrow
    else:
        microbit.display.show(target_action)
    
    #Now, wait for the user to make an action (or take too long)
    
    #1. Button A:
    if microbit.button_a.was_pressed():
        print("A")
        #Then, determine if this action was correct or not...
        if target_action == "A":
            print("Correct!")
            target_action = random.choice(choices)
            # increase score, maybe show short animation/icon
            # so the user knows they got a point
            start_time = time.time() #reset timer to 0
        else:
            print("Incorrect - Game Over")
            break
        
    #2. Shake Mechanic
    motion = microbit.accelerometer.get_z()
    if motion > 1500 or motion < -1500:
        print("Shake")
        time.sleep(0.5) #"No Shake" buffer
        
        #next, check if a shake was the correct action or not
        
    #3. Button B
        
    #4. Tilt Left
        
    #5. Tilt Right
        
    #6. Check if time_elapsed is too large (ran out of time)
    
   