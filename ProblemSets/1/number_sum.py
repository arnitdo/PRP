def sum_upto(i):
    sum = 0
    while i > 0:
        sum += i
        i -= 1
    return sum

maxNum = int(input("Enter i : "))
numSum = sum_upto(maxNum)
print("Sum is", numSum)
