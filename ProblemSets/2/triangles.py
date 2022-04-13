# Left leaning triangle
rowCount = 5
for row in range(1, rowCount + 1):
    for col in range(row):
        print("*", end = "")
    print()

# Right leaning triangle
for row in range(1, rowCount + 1):
    for col in range(rowCount - row):
        print(" ", end = "")
    for col in range(row):
        print("*", end = "")
    print()