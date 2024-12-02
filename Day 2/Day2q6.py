# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . replace the index element of list with new value and display the same
#
# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
ipl_last_index =len(ipl) -1
index,new_team = input("Enter index and new team name followed by commas").split(",")
index= int(index)
if int(index) > ipl_last_index:
    print(f"Enter a number below {ipl_last_index}")
ipl[index]=new_team
print(ipl)


