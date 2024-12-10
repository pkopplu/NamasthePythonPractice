# 2- write a Python function which takes a positive number as input and return the factorial of the number.

def factorial(num):
    product=1
    for number in range(1,int(num)+1):
        product*=number
    return product


number = input("Enter a number")
print(f" The factorial of {number} is {factorial(number)}")