# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.
numbers = [45,90,67,98,46,9,3,90,890,668,4567,98780,98789,78966]
max=numbers[0]
for num in numbers:
    if max<=num:
        max=num
print(max)