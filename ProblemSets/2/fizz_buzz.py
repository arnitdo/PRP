for num in range(51):
    if (not num % 15):
        print("FizzBuzz")
    elif (not num % 3):
        print("Fizz")
    elif (not num % 5):
        print("Buzz")
    else:
        print(num)