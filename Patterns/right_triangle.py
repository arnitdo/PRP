char = "*"
rowCount = 5
for row in range(rowCount):
    for column in range(rowCount - 1 - row):
        print(" ", end = "\t")
    for column in range(row):
        print(char, end = "\t")
    print()