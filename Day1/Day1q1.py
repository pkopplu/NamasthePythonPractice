# 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
#
# BMI = weight / (square of height)

def q1(weight, height):
    BMI = weight/height**2
    return BMI

w = float(input("enter your weight in kilogram\n"))
h = float(input("enter your height in metres\n"))
BMI = q1(w,h)
# rounding off the BMI to 2 decimals
BMI = round(BMI,2)
print(f"The BMI is {BMI}")
