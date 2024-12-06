# 6- write a program to take a positive number as input from user. if the user enters negative number
# then keep promting him to enter positive number until he enters the positive number and then print the same

def enterPositiveNumber():
    try:
        num = int(input("Enter a positive number: "))
        while num<=0:
            print("Positive please")
            num = int(input("Enter a positive number: "))
        print(f"Positive number you entered is {num}")
    except Exception as e:
        print(e)

enterPositiveNumber()
