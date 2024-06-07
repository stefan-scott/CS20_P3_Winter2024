# Microbit Image Functions
# Mr. Scott
# June 6, 2024

import microbit, time, random

#2D List
grid = [ [0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2],
         [4, 4, 4, 4, 4],
         [6, 6, 6, 6, 6],
         [8, 8, 8, 8, 8] ]

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

# CREATE AN ANIMATION
# 1. Fading Screen
while True:
    for i in range(10):   #FADE IN
        set_all(i)
        time.sleep(0.01)
    for i in range(8, 0, -1):
        set_all(i)
        time.sleep(0.01)
    #0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1



