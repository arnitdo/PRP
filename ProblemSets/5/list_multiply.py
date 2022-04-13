myList = []
for count in range(5):
    inputValue = int(input("Enter element : "))
    myList.append(inputValue)

product = 1
for num in myList:
    product *= num

print("The product of all elements is :", product)