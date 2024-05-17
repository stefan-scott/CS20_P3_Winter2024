# Reading Data from Files Demo
#
# Typically, the file we want to open should be
# Located in the same folder as our .py file

#First Step: open the file
my_file = open("poem.txt", "r") #'r' → open for READING

# OPTION ONE - read whole file into a string
# full_text = my_file.read()   # typically from here we would
                             # split up the string somehow

# OPTION TWO - read each line and store in a list
lines = my_file.readlines()

# Strip out the newline character for each line
for i in range(len(lines)):  #i: 0  1  2
    lines[i] = lines[i].rstrip("\n")

print(f"""A poem:
{lines[0]}
{lines[1]}
{lines[2]}""")

#Last Step:
my_file.close()