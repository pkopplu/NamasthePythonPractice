# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user,
# the output should be "olleH"

# def reverse_string(s):
#     l =len(s)-1
#     reversed =""
#     while l>=0:
#         reversed+=s[l]
#         l-=1
#     return reversed
#

def reverse_string(s):
    reversed=""
    for char in s:
        reversed=char+reversed
    return reversed
s=input("enter a string")
print(reverse_string(s))