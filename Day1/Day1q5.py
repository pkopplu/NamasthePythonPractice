# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string.
# if 'a' is not there then return -1.
def getAinName(name):
    name=name.lower()
    return name.find('a')

n="Swathi"
print(getAinName(n))