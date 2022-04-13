import string

inputString = input("Enter string : ")

symbolCount = 0
letterCount = 0
numberCount = 0
whitespaceCount = 0

for char in inputString:
    if char in string.digits:
        numberCount += 1
    elif char in string.ascii_letters:
        letterCount += 1
    elif char in string.whitespace:
        whitespaceCount += 1
    else:
        symbolCount += 1

print(f"Letters : {letterCount}\nNumbers : {numberCount}\nWhitespace : {whitespaceCount}\nSymbols : {symbolCount}")