# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
uni_dict={}
for uni in universities:
    name = uni[0]
    stats = {
        "students":uni[1],
        "tuition":uni[2]
    }
    uni_dict[name]=stats
print(uni_dict)

