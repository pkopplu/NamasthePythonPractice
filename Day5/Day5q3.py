# 3- Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def countUpperLower(sentence):
    uppercase,lowercase=0,0
    for char in sentence:
        if char.isupper():
            uppercase+=1
        if char.islower():
            lowercase+=1
    return uppercase,lowercase

sentence = input("Enter a sentence to count upper and lower case characters: ")
uppercase,lowercase = countUpperLower(sentence)
print(f"The number of upper case characters : {uppercase}")
print(f"The number of lower case characters : {lowercase}")