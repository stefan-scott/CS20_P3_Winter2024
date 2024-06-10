# Microbit Sprite Control
# Mr. Scott
# June 7, 2024

import microbit, time, random

#2D List
grid = [ [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]

# LED Helper Functions
def print_grid():
    #prints out grid in an easy-to-read format
    for row in grid:
        print(row)

def show_grid():
    #convert our 2D list into a string, and display
    result = ""
    for row in grid:
        for pixel in row:
            result = result + str(pixel)
        result = result + ":"
    result = result[0:-1]
    print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x,y,intensity):
    #set a pixel at (x,y) to a brightness (0-9)
    grid[y][x] = intensity
    show_grid()

def plot(x,y):
    #turn on pixel at x,y (full intensity)
    set_pixel(x,y,9)

def unplot(x,y):
    #turn off pixel at x,y
    set_pixel(x,y,0)

def queue_pixel(x,y,intensity):
    #modify pixel value, but don't display yet
    grid[y][x] = intensity

def set_all(intensity):
    #turn all pixels in the grid to INTENSITY
    for x in range(5): #0, 1, 2, 3, 4
        for y in range(5): #0, 1, 2, 3, 4
            queue_pixel(x,y,intensity)
    show_grid()


# --------------------------------------
#      Today's Demo Begins Here...
# --------------------------------------

show_grid() # Clear Screen, since 2D list is all 0s
player_x = 2
player_y = 2

plot(player_x, player_y)

while True:
    queue_pixel(player_x, player_y, 0)
    #look to change those variables based on inputs
    x = microbit.accelerometer.get_x() #-1000 to 1000
    if x < -300:    # TILT LEFT
        player_x = player_x - 1
        if player_x < 0:
            player_x = 0
    if x > 300:  # TILT RIGHT
        player_x += 1 
        player_x = min(player_x, 4)
    y = microbit.accelerometer.get_y()
    if y < -300: # FORWARD
        player_y = max(player_y - 1, 0)
    if y > 300: # BACKWARD
        player_y = min(player_y + 1, 4)      
    
    plot(player_x, player_y)
    time.sleep(0.1)






