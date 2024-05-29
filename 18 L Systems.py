# L-Systems Demo
# Mr. Scott
# May 29, 2024

# Set up Turtle Graphics
import turtle
t = turtle.Turtle()   #create Turtle and Screen
wn = turtle.Screen()
wn.setup(800,800)

t.speed(0)  #fast

t.up()
t.goto(-400,0)   #set initial position
t.down()

turtle.tracer(False) #turns off drawing

# Create the L-System
def apply_rules(ch):
    #Apply the rules to a single character
    if ch=="X":      
        return "YF+XF+Y"
    elif ch=="Y":    
        return "XF-YF-X"
    else:
        return ch

def process_string(original_str):  # ABBA
    #Loop through our original_str an apply rules to each character
    next_str = ""
    for c in original_str:
        next_str = next_str + apply_rules(c)
    return next_str

def create_L_system(num_generations, axiom):
    #Run L-System for num_generations generations
    current_gen = axiom
    for i in range(num_generations):
        next_gen = process_string(current_gen)
        current_gen = next_gen
    return current_gen

def draw_L_system(instructions, angle, distance):
    # Have the turtle make a drawing based on our
    # L-System instructions
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
#MAIN CODE HERE - Angle | Axiom
commands = create_L_system(8, "FX")
print(commands)
draw_L_system(commands, 60, 2)
turtle.update() #draw the screen    
    