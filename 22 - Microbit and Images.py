# Microbit and Images
# Mr. Scott
# June 5, 2024
# Using the built-in Images with micro:bit

# install library: Tools → Package Manager → cs20-microbitio
# "Could not get a prompt" → press RESET on mbit, then run

import microbit, time
print(microbit.Image.STD_IMAGE_NAMES)

# Display a Single Built-in Image
microbit.display.show(microbit.Image.YES)

# Display an Animation
clocks = microbit.Image.ALL_CLOCKS

# for hour in clocks:
#     microbit.display.show(hour)
#     time.sleep(0.3)

# Loop by Index with a while loop.
i = 0    # 0, 1, 2, 3, ... , 11 → 0
ani_delay = 0.2
while True:
    hour = clocks[i]
    microbit.display.show(hour)
    i += 1
    if i > 11:
        i = 0
    # Allow the user to modify the animation speed
    # Button A → faster     Button B → slower
    # 0.01 - 0.4
    if microbit.button_a.is_pressed():
        ani_delay -= 0.01
        if ani_delay < 0.01:
            ani_delay = 0.01
            
    if microbit.button_b.is_pressed():
        ani_delay += 0.01
        if ani_delay > 0.4:
            ani_delay = 0.4
    time.sleep(ani_delay)
    
    
    
