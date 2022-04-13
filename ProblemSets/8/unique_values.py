sampleData = [
    {"V" : "S001"},
    {"V" : "S002"},
    {"VI" : "S001"},
    {"VI" : "S005"},
    {"VII" : "S005"},
    {"V" : "S009"},
    {"VIII" : "S007"}
]

# valueSet = set()
#
# for dataDict in sampleData:
#     valueSet.add(dataDict[list(dataDict.keys())[0]])

valueSet = set(dataDict[list(dataDict.keys())[0]] for dataDict in sampleData)

# Or, easier

valueSet2 = set(value for [value] in [list(data.values()) for data in sampleData])


# Actual code for reals
valueSet3 = set()
for data in sampleData:
    for key, value in data.items():
        valueSet3.add(value)

print(valueSet)
print(valueSet2)
print(valueSet3)
