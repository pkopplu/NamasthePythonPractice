# 4- write a program which takes city name from user input. irrespective of in which case user enters the city name,
# print the city name in camel case meaning first letter should be capital and rest in small.
#
# example : input : MYSORE ,  print - > Mysore
def camelCase(city):
    # #wrong, strings are immutable, remember?
    # city[:1] = city[:1].upper()
    # city[1:] = city[1:].lower()
    chars =city.lower()
    chars =list(chars)
    print(chars)
    chars[0]=chars[0].upper()
    c = ''.join(chars)
    return c
city = "MYSORE"
camel_city = camelCase(city)
print(camel_city)


