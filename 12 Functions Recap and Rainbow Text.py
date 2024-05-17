# Rainbow Text + Functions Recap
# Mr. Scott
# April 26, 2024

from colorama import Fore, Back, Style


def rainbow_text(input_text):
    # style the input_text with rainbow colors
    # and return the styled string
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]   #OOB
    #             0         1             2          3            4           5  6 7 8
    output_text = Style.BRIGHT  # "" also could start with empty string
    color_index = 0
    
    for letter in input_text:
        output_text = output_text + colors[color_index]
        output_text += letter  # output_text = output_text + letter
        
        color_index += 1  #now advance the color
        if color_index >= len(colors):
            color_index = 0   #wrap around code
            
    return output_text

print( rainbow_text("Centennial Collegate, Saskatoon SK Canada") )




# Function taking input, but no return value
# non-fruitful
def func_a(a, b, c):
    # a, b, c → string type data
    # function joins a, b, and c together and prints
    print(f"{a}{b}{c}")
 
def func_b(a, b, c):
    # a, b, c → string type data
    # joins a,b,c and RETURNS
    return f"{a}{b}{c}"

# func_a("a","b","c") #prints "abc" within the function
# result = func_b("a","b","c") #returns "abc" to function call
