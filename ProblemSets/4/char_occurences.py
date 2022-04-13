import string

charMap = {char : 0 for char in string.ascii_letters}

string = input("Enter a string : ")
for char in string:
    if char not in charMap.keys():
        continue
    else:
        charMap[char] += 1

for char, count in charMap.items():
    if count == 0:
        continue
    else:
        print(f"{char} occurred {count} times in the string")