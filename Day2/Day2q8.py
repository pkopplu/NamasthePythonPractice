# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list.
# Display the old list , new list,length of original and new list
#
# example : input : 2,SRH
# output :
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6

ipl= ['CSK','MI','KKR','LSG','PBKS']
index,team =input("Enter a index and team name").split(",")
index=int(index)
team=team.strip().upper()
print(f"old list: {ipl} and length {len(ipl)}")
ipl.insert(index,team)
print(f"new list: {ipl} and length {len(ipl)}")



