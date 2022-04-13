print("Enter 10 tuple elements : ", end = "")
tempList = []
for count in range(10):
    num = int(input())
    tempList.append(num)

myTuple = tuple(tempList)
print(f"Tuple is {myTuple}")
print(f"Fourth element (from front) = {myTuple[3]}")
print(f"Fourth element (from rear) = {myTuple[-4]}")