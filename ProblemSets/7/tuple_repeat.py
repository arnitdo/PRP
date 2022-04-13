print("Enter 10 tuple elements : ", end = "")
tempList = []
for count in range(10):
    num = int(input())
    tempList.append(num)

myTuple = tuple(tempList)
elementMap = dict()
for element in myTuple:
    if element in elementMap.keys():
        elementMap[element] += 1
    else:
        elementMap[element] = 1

for key, value in elementMap.items():
    if value > 1:
        print(f"{key} was repeated {value} times!")