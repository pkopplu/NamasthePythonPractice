# 3- given a list list1=[1,2,3,4,5,6,7,8]
# diplay a new list which contains only odd position index values from above list.

list1=[1,2,3,4,5,6,7,8]
# new_list =[list1[i] for i in range(len(list1)) if i%2!=0]
# print(new_list)

new_list = list1[1::2]
print(new_list)