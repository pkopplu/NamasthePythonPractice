# 3- write a program to take state as input from user and print the capital of the state using above dictonary.
# If the state is not there in dictonary then print "sorry , information not available"

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
keys_list = list(capitals_dict.keys())
keys_list = [k.upper() for k in keys_list]
print(keys_list)
state=input("Enter the state to know its capital").upper()
if state not in keys_list:
    print("sorry, information not available")
else:
    print(f"The capital of {state.capitalize()} is {capitals_dict[state.capitalize()]}")