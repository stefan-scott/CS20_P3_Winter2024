# Regular Polygons
# Mr. Scott
# April 30, 2024
# Looking for patterns + drawing with the turtle

# Turtle "boilerplate" or setup code
import turtle

window = turtle.Screen()  #creates a canvas window


roscoe = turtle.Turtle()  #creates a turtle object
roscoe.color("coral")
roscoe.pensize(4)

anna = turtle.Turtle() # Make a second turtle...
anna.color("blue")

# Functions
def triangle():
    # draw a 100x100 equilateral triangle
    for i in range(3):  #repeat 3:
        roscoe.fd(100)
        roscoe.lt(120)

def square(my_turtle, side_length):
    # draws a square using the turtle library
    # my_turtle → turtle object
    # side_length → integer, for length of each side
    for i in range(4):  # repeat 4:
        my_turtle.fd(side_length)
        my_turtle.left(90)

def pentagon(my_turtle, side_length):
    # my_turtle → turtle object
    # side_length → integer, for length of each side
    for i in range(5):  #repeat 5
        my_turtle.fd(side_length)
        my_turtle.left(72)

def r_poly(my_turtle, num_sides, side_length):
    # my_turtle → turtle object
    # num_sides → number of sides for this polygon
    # side_length → integer, for length of each side
    for i in range(num_sides):
        my_turtle.fd(side_length)
        my_turtle.lt(360/num_sides)
        
# Main Code
roscoe.speed(0)
roscoe.pensize(2)

for n in range(3, 30):  #[3, 4, 5, 6, ..., 29]
    r_poly(roscoe, n, 20)


# for length in range(20, 200, 10):  #[20, 30, 40, 50, ..., 190]
#     pentagon(roscoe, length)
#     pentagon(anna, length-1)

# square(roscoe,100)
# square(anna, 75)

# triangle()

# End Program
window.exitonclick()

