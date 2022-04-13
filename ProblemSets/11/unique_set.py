l1 = list(range(5, 16))
l2 = [10, 20, 12, 15, 14]

s1 = set(l1)
s2 = set(l2)

unique = s2 - s1
print(unique)