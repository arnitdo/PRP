myList = []
for i in range(5):
    num = int(input("Enter an element : "))
    myList.append(num)

smallest = myList[0]
largest = myList[4]

for num in myList:
    if num <= smallest:
        smallest = num
    if num >= largest:
        largest = num

print(f"Smallest number : {smallest}\nLargest number : {largest}")