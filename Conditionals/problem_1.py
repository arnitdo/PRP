# Write a script to check if mail ID Is correct by checking if it contains the character @ and .com

def emailStatusStringify(emailValid):
    emailStatusMap = {
        True : "Valid Email!",
        False : "Invalid Email"
    }
    return emailStatusMap.get(emailValid, "Could not determine validity of entered EMail!")

def emailCheck():
    email = input("Enter email : ")
    emailValid = False
    if "@" in email and ".com" in email:
        emailValid = True
    print(emailStatusStringify(emailValid))

emailCheck()










# Quick regex for email : [\w( .)]+@\w+\.[a-zA-Z(. )]{2,}