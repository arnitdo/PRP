import string

inputString = input("Enter a string : ")

lowercaseString = ""
uppercaseString = ""
for char in inputString:
    if char in string.ascii_lowercase:
        lowercaseString += char
    elif char in string.ascii_uppercase:
        uppercaseString += char
    else:
        continue

outputString = lowercaseString + uppercaseString

print(f"Lowercase-first string is : {outputString}")