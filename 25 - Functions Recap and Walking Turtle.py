# Functions Recap and Walking Turtle
# Mr. Scott
# June 10, 2024

# 2. Randomly Walking Turtle...
import turtle, random

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.color(random.choice(colors))
speed = 8

wn = turtle.Screen()
wn.setup(700,700)

def is_on_screen(current_turtle): #Boolean Function
    # check if the current_turtle is on the
    # screen. Return True if so, False if not.
    x = current_turtle.xcor()
    y = current_turtle.ycor()
    if x > -350 and x < 350:
        if y > -350 and y < 350:
            return True
    return False

# Implement the random walk algorithm
turtle.tracer(False) #turns off drawing the screen
while True:
    roll = random.randint(0,3) #0, 1, 2, 3
    if roll == 0:
        t.setheading(0) #EAST
    elif roll == 1:
        t.setheading(90) #NORTH
    elif roll == 2:
        t.setheading(180) #WEST
    else:
        t.setheading(270) #SOUTH
    
    t.fd(speed)
    turtle.update() #update the screen
    
    if not is_on_screen(t): #reset turtle
        t.up()
        t.goto(0,0)
        t.down()
        t.color(random.choice(colors))
        t.pensize(random.randint(1,4))
        speed = random.randint(3,8)
        







# # 1. Function to "triple" a string
# 
# # S I G N A T U R E
# #      name    (parameter list)
# def triple_string(str):
#     # Takes a given string, and returns that
#     # Same string, repeated 3 times...
#     # str → String, the string to repeat
#     # "abc" → "abcabcabc"
#     return str*3 #exits function and sends the
#         #data back to the function call
# 
# result = triple_string("abc")
# print(triple_string("wow"))
# print(triple_string(triple_string("a")))
