def factorial(num):
    if num < 0:
        print("Factorials of negative numbers cannot be calculated!")
        exit()
    fact = 1
    while num:
        fact *= num
        num -= 1
    return fact

number = int(input("Enter a number to find factorial : "))
factorialValue = factorial(number)
print(f"The factorial of {number} is {factorialValue}")