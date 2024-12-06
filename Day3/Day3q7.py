#
# 7- consider the below list of list contains following information :
#
# 1. The name of a university
# 2. The total number of enrolled students
# 3. The annual tuition fees
#
# universities = [
# ['California Institute of Technology', 2175, 37704],
# ['Harvard', 19627, 39849],
# ['Massachusetts Institute of Technology', 10566, 40732],
# ['Princeton', 7802, 37000],
# ['Rice', 5879, 35551],
# ['Stanford', 19535, 40569],
# ['Yale', 11701, 40500]
# ]
#
# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together
# 3- mean of tuition fees

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def returnUniversities(universities):
    university_list=[university[0]for university in universities]
    return university_list

def countStudents(universities):
    student_counts = [university[1]for university in universities]
    return sum(student_counts)

def mean_tuition(universities):
    tuition_fees = [university[2] for university in universities]
    mean_tuition = sum(tuition_fees)/len(tuition_fees)
    return mean_tuition

print(f"The university list is {returnUniversities(universities)}")
print(f"The total student count is {countStudents(universities)}")
print(f"The mean tuition fee is {mean_tuition(universities)}")

