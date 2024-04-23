# Choosing randomly from a list

import random


nouns = ["","","","",""]
verbs = []
adj = []

fruit = ["apple", "banana", "cantaloupe", "durien"]
#           0        1           2            3 (len-1)
#           -4       -3          -2           -1

len_of_list = len(fruit) #returns length of the list

# Approach One:   Generate a random (valid) index
# index = random.randint(0, len_of_list-1)
# item = fruit[index]
# print(item)

# Approach Two:  Pick randomly from a list
item = random.choice(fruit) #will choose one thing from list
print(item)