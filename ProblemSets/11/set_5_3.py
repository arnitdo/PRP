set_a = set(range(5, 56, 5))
set_b = set(range(3, 34, 3))
set_all = set_a.union(set_b)
set_unique = set_a.symmetric_difference(set_b)

print(set_a)
print(set_b)
print(set_all)
print(set_unique)