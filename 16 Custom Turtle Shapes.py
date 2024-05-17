# Custom Turtle Shapes
# Mr. Scott
# May 6, 2024
# Custom Shapes by Coordinates, by image file (GIF)

# Turtle SETUP
import turtle
window = turtle.Screen()
t = turtle.Turtle()

# Register Shape - by coordinates
new_shape = ((30,0), (0,30), (-30,0), (0,-30)) #tuple
turtle.register_shape("diamond", new_shape)
t.shape("diamond")

# Argyle Pattern
t.speed(0)
t.up()
start_x = -200
start_y = 200
t.goto(start_x, start_y)

for j in range(5):  #make 5 rows...
    # Algorithm for single row (start facing east)
    for i in range(5):   # + advancing cursor
        t.stamp()
        t.forward(60)
    start_y = start_y - 60
    t.goto(start_x, start_y)


# Register Shape by Image (GIF)
# A few things about using images:
# - .gif only  , static image
# not all gifs have transparent backgrounds
#      -use an online tool, to resave with one
# image rotation is fixed. doesn't show heading
turtle.register_shape("turtle_image.gif")
t.shape("turtle_image.gif")
t.speed(2)
t.left(60)
t.forward(400)






window.exitonclick() #MUST be last statement