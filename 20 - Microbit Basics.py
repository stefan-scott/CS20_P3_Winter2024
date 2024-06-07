# Microbit Basics
# USER INPUT → Button Presses
# OUTPUT → LED (Text)
# SENSOR → Accelerometer

import microbit, time

# TEXT OUTPUT - static and animated
# SHOW - static
# for letter in "SASKATCHEWAN":
#     microbit.display.show(letter)
#     time.sleep(0.3)   #delay 0.3s

# SCROLL  - slide text right to left
# print("test to the shell")
# microbit.display.scroll("SASKATCHEWAN")

# BUTTON PRESSES (Button A, Button B)
# a_presses = 0
# b_presses = 0
# while a_presses < 50 and b_presses < 5:
#     if microbit.button_a.is_pressed():
#         a_presses += 1
#         print(f"a: {a_presses}\t b:{b_presses}")
#     if microbit.button_b.was_pressed():
#         b_presses += 1
#         print(f"a: {a_presses}\t b:{b_presses}")

#ACCELEROMETER (orientation of micro:bit)
while True:
    x = microbit.accelerometer.get_x() #ROLL Rotation
    if x < -300:
        print("LEFT")
    elif x > 300:
        print("RIGHT")
    else:
        print("FLAT")
        
#     print(x)  # -1000 to 1000    
    #-1000     |       0       |       1000
    # LEFT   -300    FLAT     300     RIGHT
    time.sleep(0.1)

