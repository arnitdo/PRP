baseString = input("Enter string : ")
shiftDelta = int(input("Enter delta to shift each character by : "))
stringLength = len(baseString)
newString = ""

for idx in range(stringLength):
    currentChar = baseString[idx]
    currentCharCode = ord(currentChar)
    shiftedCharCode = currentCharCode + shiftDelta
    if shiftedCharCode < 32 or shiftedCharCode > 127:
        print("Non-printable ASCII character encountered! Current character will not be replaced!")
        shiftedChar = currentChar
    else:
        shiftedChar = chr(shiftedCharCode)
    newString += shiftedChar

print("Cyphered text is", newString)