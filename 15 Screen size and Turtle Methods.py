# Screen Size + Turtle Methods
# Mr. Scott
# May 3, 2024
# Creating a custom window, penup(), pendown(), shape() stamp()

# Turtle Graphics Setup Code
import turtle, random

window = turtle.Screen() # 800x800
window.setup(500,400)

francis = turtle.Turtle()
francis.color("blue")

# Main Program

# PART TWO
def hollow_c(my_turtle):
    long = 100
    short = 10
    
    for i in range(3):
        my_turtle.fd(long)
        my_turtle.left(90)
        
    my_turtle.fd(short)
    my_turtle.left(90)
    
    #inner three lines
    for i in range(3): #[0, 1, 2]
        my_turtle.fd(long-short)
        if i == 1:
            my_turtle.back(short)
        my_turtle.right(90)
    
    my_turtle.left(180)
    my_turtle.fd(short)
    my_turtle.left(90)
    
francis.speed(0)
for i in range(30):
    hollow_c(francis)
    francis.left(12)









# PART ONE
# francis.shape("turtle")  #circle, square, classic, arrow, turtle
# francis.up()  #.penup() | .up()
# 
# def draw_x():
#     for i in range(10,300,10):  #[10, 20, 30, 40 ... 280, 290]
#         francis.fd(i)
#         francis.left(90)
#         francis.stamp() #leaves an 'impression' of the turtle
# 
# francis.speed(0)
# for i in range(500):
#     x = random.randint(-250,250)
#     y = random.randint(-200,200)
#     francis.goto(x,y)
#     francis.stamp()


window.exitonclick() #MUST be last instruction