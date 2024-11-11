# 3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float)
# and print the expected total amount  after  2 years.
#
# example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121

def totalAfter2Years(principal, rate):
    return principal*(1+rate/100)*(1+rate/100)

p = 100
r = 10
total = round(totalAfter2Years(p,r),2)
print(f"The amount after 2 years is {total}")

