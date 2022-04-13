import json

tupleList = [
    ("name", "Arnav"),
    ("surname", "Deo"),
    ("roll", "S143"),
    ("department", "CSE"),
    ("semester", 4)
]

dictionary = dict()

for tup in tupleList:
    dictionary[tup[0]] = tup[1]

print(json.dumps(dictionary, indent = 4))