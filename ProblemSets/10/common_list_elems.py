list_a = [1, 2, 3 ,4, 6, 8, 9, 10]
list_b = [2, 4, 6, 8, 10]

list_a_set = set(list_a)
list_b_set = set(list_b)

common_elements = list_a_set.intersection(list_b_set)

common_list = list(common_elements)

print(f"Common elements in {list_a} and {list_b} are {common_list}")