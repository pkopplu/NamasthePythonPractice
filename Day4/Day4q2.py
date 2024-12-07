# 2- given below dictonaries of states and their capital:
#
# capitals_dict = {
# 'Alabama': 'Montgomery',
# 'Alaska': 'Juneau',
# 'Arizona': 'Phoenix',
# 'Arkansas': 'Little Rock',
# 'California': 'Sacramento',
# 'Colorado': 'Denver',
# 'Connecticut': 'Hartford',
# 'Delaware': 'Dover',
# 'Florida': 'Tallahassee',
# 'Georgia': 'Atlanta',
# }
#
# pick a state from above dictonary and ask user to enter the capital of the state.If the user answers incorrectly,
# then repeatedly ask them for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without
# guessing correctly, display the correct answer and the word "Goodbye".
#
# Note: Make sure the user isn’t punished for case sensitivity. In other words, a guess of "Denver"
# is the same as "denver". Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".
#
#
import random as r

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

#pick a random state
state = r.choice(list(capitals_dict.keys()))
print(f"Enter the capital for {state}")
capital = input()
capital = capital.upper()
while capital != capitals_dict[state].upper():
    #capital=input()
    capital=capital.upper()
    if capital=="EXIT":
        print(f"The capital for {state} is {capitals_dict[state]} ")
        print("Goodbye!")
        break
    elif capital == capitals_dict[state].upper():
        print("Correct")
        break
    print("Enter the correct capital or exit")
    capital = input()

