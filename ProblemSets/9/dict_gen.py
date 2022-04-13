# n = int(input("Enter n : "))
# squares = {num : num * num for num in range(1, n + 1) } # Shorthand method
# print(squares)
#
# squares2 = dict()
# for i in range(1, n + 1):
#     squares2[i] = i * i
#
# print(squares2)

# Also one liner
print({num : num * num for num in range(1, int(input("Enter n : ")) + 1)})