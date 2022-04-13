def isPrime(num):
    if num <= 1:
        return False
    if num > 2 and not (num % 2):
        return False
    else:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
    return True


start = int(input("Enter start of range : "))
end = int(input("Enter end of range : "))

if start < 0 or end < 0:
    print("Invalid Input!")
    exit()

for num in range(start, end + 1):
    prime = isPrime(num)
    if prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
