# Microbit and Turtle Control
# Mr. Scott
# June 4, 2024
# Also include a little recap on FUNCTIONS (parameters, return)

# Tools → Package Manager → Search:  cs20-microbitio
import microbit, turtle, time, random

#Turtle Setup
racer_a = turtle.Turtle()
racer_a.shape("turtle")
racer_a.color("red")

racer_b = turtle.Turtle()
racer_b.shape("turtle")
racer_b.color("blue")

wn = turtle.Screen()
wn.setup(800,400)

# Function Practice
def horizontal_tilt(sensitivity):
    # report the horizontal position of microbit(left,right,flat)
    # sensitivity → num determining how much rotation causes
    # a non-flat reading
    x = microbit.accelerometer.get_x()
    if x < sensitivity * -1:   
        return "left"
    elif x > sensitivity:
        return "right"
    else:
        return "flat"

# Set up the Race
judge = turtle.Turtle()
judge.up()
judge.goto(300,-150)
judge.down()
judge.goto(300, 150)

racer_a.up()
racer_a.goto(-300,50)

racer_b.up()
racer_b.goto(-300, -50)

# Conduct the Race
# Race 1: CPU vs CPU
# while racer_a.xcor() < 300 and racer_b.xcor() < 300:
#     racer_a.fd(random.randint(4,7))
#     racer_b.fd(random.randint(4,7))
# if racer_a.xcor() > racer_b.xcor():
#     print("RACER A WINS")
# else:
#     print("RACER B WINS")

# Race 2: CPU vs Human

last_move = "flat"
while racer_a.xcor() < 300 and racer_b.xcor() < 300:
    #CPU
    racer_a.fd(random.randint(2,5))
    
    #Accel-adv   using our horizontal_tilt() function
    #handcar mechanism
    current = horizontal_tilt(300)
    if current != "flat" and current != last_move:
        speed = 15
        last_move = current
    else:
        speed = 0
    racer_b.fd(speed)
    
wn.exitonclick()
        




#Human (accel_simple, buttons, accel_adv)
    #Accel-Simple
#     x = microbit.accelerometer.get_x() #-10   to 10
#     speed = x/100
    
    #Button Press (was_pressed())
#     if microbit.button_a.was_pressed():
#         speed = 8
#     else:
#         speed = 1.5
    


