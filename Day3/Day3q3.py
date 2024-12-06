# 3- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers
#even_list = []
#odd_list = []
def create_even_odd_lists(l):
    even_list = [i for i in l  if i%2==0]
    odd_list = [i for i in l if i%2!=0]
    return even_list,odd_list

l = [2,4,67,90,57,38,93,29]
even_list, odd_list = create_even_odd_lists(l)
print("even list: " +str(even_list))
print("odd list:" +str(odd_list))
