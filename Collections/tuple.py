myTuple = ("Eggs", "Spam")
myIntegerTuple = (10, 20)
myMixedTuple = myTuple + myIntegerTuple
print(myMixedTuple)

myNestedTuple = (myTuple, myIntegerTuple)
print(myNestedTuple)

myMultipliedTuple = myTuple * 3
print(myMultipliedTuple)

print(f"ID of original myTuple is {id(myTuple)}")
myTuple = ("Foo", "Bar")

print(f"New ID of myTuple is {id(myTuple)}")

try:
    myTuple[0] = 3
except TypeError as e:
    print(e)
    print("Tuples are mutable!")

myTupleSlice = myMultipliedTuple[1:-1]
print(myTupleSlice)

myList = [0, 1, 2]
myNewTuple = tuple(myList)
print(myNewTuple)

myString = "FizzBuzz"
myStringTuple = tuple(myString)
print(myStringTuple)

myDict = {
    "rollnumber"    : 43,
    "name"          : "Arnav Deo"
}

myDictTuple = tuple(myDict)
print(myDictTuple)

mySecondTuple = ("Java", "Python", "C++", "Kotlin")
for enum, value in enumerate(mySecondTuple):
    print(f"{enum} : {value}")

print(max(mySecondTuple))
print(min(mySecondTuple))
print(sorted(mySecondTuple))
print(any(mySecondTuple))

import timeit
print(timeit.timeit("x = (1, 3, 5, 7, 9)"))
print(timeit.timeit("x = [1, 3, 5, 7, 9]"))