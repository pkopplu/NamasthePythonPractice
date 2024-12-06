# 2- given a list of numbers unsorted, write a program to find the median of the numbers in list

def medianList(l):
    l.sort()
    if len(l)%2==0:
        mid= len(l)//2
        return (l[mid-1]+l[mid])/2
    else:
        mid = len(l)//2
        return l[mid]



l=[7,4,8,93,98,87,3,90,56]
print(medianList(l))