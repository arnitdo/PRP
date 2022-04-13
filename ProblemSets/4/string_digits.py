string = input("Enter a numeric string : ")
sum = 0
average = 0
numCount = 0
for char in string:
    ascii_ordinal = ord(char)
    if (ascii_ordinal < ord('0') or ascii_ordinal > ord('9')):
        continue
    else:
        true_value = ascii_ordinal - 48
        sum += true_value
        numCount += 1

average = sum / numCount
print(f"Sum : {sum}, Average : {average}")