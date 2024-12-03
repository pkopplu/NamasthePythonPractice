# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple
# first name : MOhit
# last name : sharma
# age 32
#
# Display : my name is Mohit Sharma and I am 32 years old.
#
# note that first letter of first name and last name both should be in capital letters and rest in small.

def display_info():
    firstName=input("first name:")
    #print("\n")
    firstName=firstName.lower()
    firstName=list(firstName)
    firstName[0]=firstName[0].upper()
    firstName =''.join(firstName)
    lastName=input("last name:")
    lastName=lastName.lower()
    lastName=list(lastName)
    lastName[0]=lastName[0].upper()
    lastName=''.join(lastName)
    #print("\n")
    age=input("age:")
    #print("\n")
    print(f"my name is {firstName} {lastName} and I am {age} years old")

display_info()