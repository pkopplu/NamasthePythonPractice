# 1- create a txt file and put 4-5 lines. Now create another file from the previous file
# and at the end of each line put the count of words.
#
# example :
# file 1:
# this is namaste sql course
# this is python course
# this assinment is part of day4 lecture
#
#
# file2:this is namaste sql course:5
# this is python course:4
# this assignment is part of day4 lecture:7

#creating the file
with open('sample.txt','w') as f:
    f.write("this is namaste sql course\n")
    f.write("this is python course\n")
    f.write("this assignment is part of day4 lecture\n")

list_lines=[]
with open('sample.txt','r') as f:
    list_lines=f.readlines()
print(list_lines)
lines_new = [ line.strip() +":"+ str(len(line.split(" "))) for line in list_lines]
print(lines_new)

with open('sample2.txt', 'w') as f:
    for line in lines_new:
        f.write(line+"\n")