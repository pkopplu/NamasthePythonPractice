# 1- write a program which takes single input from user contaning first name,last name and age as
# comma separated value and display then in 3 lines in given format below.
#
# example user input : Ankit,Bansal,35
#
# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old
#
# note : do not hardcode name at any place

def name_age():
    comma_values = input("Please enter first name, last name and age separated by commas")
    details = comma_values.split(",")
    print(f"First name is {details[0]}")
    print(f"last name is {details[1]}")
    print(f"{details[0]} is {details[2]} years old")

name_age()