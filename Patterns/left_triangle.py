char = "*"
numRows = int(input("Enter number of rows : "))
for row in range(1, numRows + 1):
    for column in range(row):
        print(char, end = "\t")
    print()