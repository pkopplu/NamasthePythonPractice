#
# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.

ipl= ['CSK','MI','KKR','LSG','PBKS']
team =input("Enter a team name")
team=team.strip().upper()
# if team in ipl:
#     print("True")
# else:
#     print("False")
team_check = team in ipl
print(team_check)