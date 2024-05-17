# Styling Text in Python
# April 25, 2024
# Mr. Scott

# Working with two more libraries: colorama,  emoji

import emoji
from colorama import Fore, Back, Style

# Test it out a bit....   :smiling_face_with_halo:
print(emoji.emojize("Testing an emoji - :smiling_face_with_halo:"))
print(emoji.emojize(":woman_vampire:  :robot:   :farmer:"))

# Try using text coloring/style
print(Fore.RED + "Red" + Fore.BLUE + "Blue" + Fore.RESET)
print(Back.YELLOW + "Yellow" + Back.MAGENTA + "Magenta" + Back.RESET)
print(Fore.GREEN + Style.DIM + "DIM" + Style.BRIGHT + "BRIGHT" +Style.NORMAL+"NORMAL")


