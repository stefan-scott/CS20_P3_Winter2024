# First Turtle Program
# Mr. Scott
# April 29, 2024
# A look at window, turtle, movement, color
#
# Reminder: NEVER name your code turtle.py

import turtle, random

# Boilerplate code → "startup code for using the turtle"
window = turtle.Screen() #creates a screen object
window.bgcolor("lightblue")

my_turtle = turtle.Turtle() #creates a turtle object
my_turtle.color("yellow")
my_turtle.pensize(4)  #number of pixels thick for the line
my_turtle.speed(0)

# PROGRAM 3 - Loops and color strings
colors = ["BlueViolet", "Coral", "DarkOliveGreen", "gold"]
num_moves = 200
for i in range(num_moves):  #[0, 1, 2, 3, ..., num_moves-1]
    my_turtle.color(random.choice(colors))
    my_turtle.forward(i)
    my_turtle.rt(60)
    
# PROGRAM 2 - A few more instructions
# my_turtle.bk(75)  #.bk() .back() .backward()
# my_turtle.rt(73)  #.rt()  .right()
# my_turtle.fd(104) #.fd()  .forward()
# my_turtle.goto(0,0)  # absolute movement to (x,y)

# PROGRAM 1 - Basic Movement
# my_turtle.forward(100)  # move forward 100 pixels
# my_turtle.left(45)      # turn CCW 45 degrees
# my_turtle.backward(150) # move backward 150 pixels

# AT THE VERY END OF YOUR PROGRAM...
window.exitonclick() #waits for a click, then closes