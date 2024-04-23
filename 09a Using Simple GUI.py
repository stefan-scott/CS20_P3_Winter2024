# Using Simple GUI
# Mr. Scott
# April 22, 2024
# Printing strings and reading strings

import PySimpleGUI as sg
# str, int, floats, bool, None

# Read in Strings from Popup:
name = sg.popup_get_text("Enter a name: ")
grade = sg.popup_get_text("Enter a grade: ")

if grade == None:
    grade = 9 #set to 9 if no grade given

# Printing String to Popup:
sg.popup(f"Welcome, {name}. You are in grade {grade}.")



