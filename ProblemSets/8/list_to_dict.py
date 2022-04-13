import json
list_a = ["name",   "surname",  "age",  "grade"]
list_b = ["Arnav",  "Deo",      17,     "A"]

kv_map = dict()

list_a_len = len(list_a)
list_b_len = len(list_b)
if list_a_len != list_b_len:
    print(f"Two lists must be of same size!")
else:
    for idx in range(list_a_len):
        key = list_a[idx]
        value = list_b[idx]
        kv_map[key] = value

print(f"Combined dictionary is -")
print(json.dumps(kv_map, indent = 4))
