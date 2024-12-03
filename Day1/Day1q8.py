# 8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.
# Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# first name : MOhit
# last name : sharma
# company : infosys
#
# Display : morma@infosys.com
#
# note full email id should -be in lower case
def createEmail():
    first_name = input("first name : ")
    first_name=first_name.lower()
    last_name = input("last name : ")
    last_name=last_name.lower()
    company = input("company : ")
    company=company.lower()
    print( f"{first_name[:2]}{last_name[-3:]}@{company}.com")

createEmail()

