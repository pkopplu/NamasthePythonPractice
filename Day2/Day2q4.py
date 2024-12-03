# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']
#
# take a ipl team name as input from user and display a list of all elements from that name.
#
# example : input : KKR
# # output : ['KKR','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
team = input("Enter a team name")
team=team.strip().upper()
if team not in ipl:
    print("Enter a name from CSK,MI,KKR,LSG,PBKS")
else:
    index= ipl.index(team)
    print(ipl[index:])