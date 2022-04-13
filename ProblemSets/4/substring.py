baseString = input("Enter a string : ")
baseSubString = input("Enter substring to find : ")

string = baseString.upper()
subString = baseSubString.upper()

firstSubChar = subString[0]
stringLen = len(string)
subStringLength = len(subString)

matchCount = 0

for charIdx in range(stringLen):
    currentChar = string[charIdx]
    if currentChar == firstSubChar:
        endIndex = charIdx + subStringLength
        if endIndex > stringLen:
            continue
        try:
            stringSlice = string[charIdx:endIndex]
            baseStringSlice = baseString[charIdx:endIndex]
            if stringSlice == subString:
                print(f"Found substring from {charIdx} to {endIndex} : {baseStringSlice}")
                matchCount += 1
        except:
            pass

print(f"Total matches : {matchCount}")