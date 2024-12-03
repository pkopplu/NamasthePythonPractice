# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']
#
# take a ipl team name as input from user and display a list of all elements except input one
#
# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
team = input("Enter a team name")
team=team.strip().upper()
if team not in ipl:
    print("Enter a name from CSK,MI,KKR,LSG,PBKS")
else:
    ipl.remove(team)
    print(ipl)