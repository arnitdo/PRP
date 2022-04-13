elements = []
while True:
    inputElement = input("Enter a value to append to the list : ")
    if inputElement == "done":
        break
    elements.append(int(inputElement))

elementSum = 0
for num in elements:
    elementSum += num

print("Sum of all elements is ", elementSum)
