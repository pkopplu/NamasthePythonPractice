# 4- Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
from operator import truediv

dict ={}
def uniqueList(l):
    for i in l:
        if i not in dict.keys():
            dict[i]= True
    print(list(dict.keys()))

sample_list = [1,2,3,3,3,3,4,5]
uniqueList(sample_list)