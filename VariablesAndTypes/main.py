someString = "Computer"
someInteger = 20
someFloat = 3.14

print(f"{someString} is of type {type(someString)}")
print(f"{someInteger} is of type {type(someInteger)}")
print(f"{someFloat} is of type {type(someFloat)}")

someBinaryNum = 0b0101
someOctalNum = 0o0713
someHexNum = 0xFF

print(f"{someBinaryNum} is of type {type(someBinaryNum)}")
print(f"{someOctalNum} is of type {type(someOctalNum)}")
print(f"{someHexNum} is of type {type(someHexNum)}")

exponentialLiteralOne = 0.6e+2  # 0.6 * 10 ^ (+2) = 0.6 * 100 = 60
exponentialLiteralTwo = 0.5e-2  # 0.5 * 10 ^ (-2) = 0.5 * 1/100 = 0.005
print(exponentialLiteralOne)
print(exponentialLiteralTwo)

booleanValueTrue = True
booleanValueFalse = False

booleanExpressionResult = (5 < 10)  # Should be True
print(booleanExpressionResult)

booleanComparisonResult = True == True  # Should be True
print(booleanComparisonResult)

numericLiteralConstant = 215
numericStringConstant = "40"

print(f"{numericLiteralConstant} is of type {type(numericLiteralConstant)}")
print(f"'{numericStringConstant}' is of type {type(numericStringConstant)}")

derivedNumericConstant = int(numericStringConstant)
numericSum = numericLiteralConstant + derivedNumericConstant

print(f"Sum of literal value ({numericLiteralConstant}) and converted value ({derivedNumericConstant}) is {numericSum}")

# Compound assignment
apples, oranges = "Apple", "Orange"

# Complex numbers

complexValue = complex(1, 3) # 1 + 3i
print(complexValue)