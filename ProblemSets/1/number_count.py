maxNumberCount = int(input("Enter n : "))
positiveCount = 0
negativeCount = 0
zeroCount = 0

for count in range(maxNumberCount):
    userNum = int(input("Enter number : "))
    if userNum < 0:
        negativeCount += 1
    elif userNum == 0:
        zeroCount += 1
    else:
        positiveCount += 1

print("Positive numbers entered :", positiveCount)
print("Negative numbers entered :", negativeCount)
print("Zeroes entered :", zeroCount)