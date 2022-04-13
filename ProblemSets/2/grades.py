gradeMap = {
    "0-39" : 0,
    "40-59" : 0,
    "60-69" : 0,
    "70-89" : 0,
    "90-100" : 0
}

for inputCount in range(10):
    marks = int(input("Enter marks : "))
    if marks < 0 or marks > 100:
        print("Invalid input!")
        continue
    for gradeKey in gradeMap:
        rangeSplit = gradeKey.split("-")
        rangeMin = int(rangeSplit[0])
        rangeMax = int(rangeSplit[1])
        if marks >= rangeMin and marks <= rangeMax:
            gradeMap[gradeKey] += 1

for key, value in gradeMap.items():
    print(f"{key} : {value} students")