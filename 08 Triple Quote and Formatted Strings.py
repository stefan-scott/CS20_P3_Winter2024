# Triple Quoted and Formatted Strings
# Mr. Scott
# April 19, 2024
# A few more ways to work with string data

# Four ways to encapsulate strings:
#   " "    ' '    """  """   ''' '''
# triple-quoted strings can span multiple lines

my_string = '''"How's it going?", he said.'''
print(my_string)

my_string2 = """Down
Down
Down
Down..."""
print(my_string2)

# Escape Sequences - special combo of chars to
# stand for something...
# \" → "   \' → '   \t → tab  \n → newline  \\→\
my_string3 = "ab\tcd\'\"e\nf\\g"
print(my_string3)

# Formatted Strings
food = "apple"        # string
sport = "soccer"      # string
time_remaining = 20   # int

story = f"""
It's time for an {food} break.
We're playing a game of {sport},
and there is {time_remaining} minutes left.
"""
print(story)
