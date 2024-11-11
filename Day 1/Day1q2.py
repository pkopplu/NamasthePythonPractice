# 2- write a program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b' and print it.

def replaceA2B(name):
    name=name.lower()
    name =name.replace("a","b")
    return name
name= "Uganda"
print(f"The name before: {name}")
replaced = replaceA2B(name)
print(f"The name after replcing a to b: {replaced}")
