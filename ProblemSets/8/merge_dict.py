import json


def dict_merger(dict_a, dict_b):
    dict_a_keys = dict_a.keys()
    dict_b_keys = dict_b.keys()

    final_dict = dict()
    dup_resolve = dict()

    for key_a in dict_a_keys:
        for key_b in dict_b_keys:
            if key_a == key_b:
                print(f"Duplicate keys found! Please select which value to use for key {key_a} - ")
                value_a = dict_a[key_a]
                value_b = dict_b[key_b]
                print(f"0 - {key_a} : {value_a}")
                print(f"1 - {key_b} : {value_b}")
                try:
                    choice = int(input("Select (default 0) : "))
                except ValueError:
                    choice = -1
                if choice == 0:
                    dup_resolve[key_a] = value_a
                elif choice == 1:
                    dup_resolve[key_b] = value_b
                else:
                    print(f"Invalid choice selected! Using choice 0 by default!")
                    dup_resolve[key_a] = value_a

    for key_a in dict_a_keys:
        value_a = dict_a[key_a]
        final_dict[key_a] = value_a

    for key_b in dict_b_keys:
        value_b = dict_b[key_b]
        final_dict[key_b] = value_b

    # Merging duplicates
    for dup_key in dup_resolve.keys():
        dup_value = dup_resolve[dup_key]
        final_dict[dup_key] = dup_value

    return final_dict

## Base case, no duplicates to be resolved

tcase_1_a = {
    "name" : "Arnav",
    "surname" : "Deo"
}

tcase_1_b = {
    "age" : 17,
    "grade" : "A"
}

## Test case 2 is to test duplicate removal

tcase_2_a = {
    "name" : "Arnav",
    "surname" : "Deo"
}

tcase_2_b = {
    "name" : "Aarav",
    "age" : 17
}


tcase_1_result = dict_merger(tcase_1_a, tcase_1_b)

print(f"Test case 1 results : {json.dumps(tcase_1_result, indent = 4)}")

tcase_2_result = dict_merger(tcase_2_a, tcase_2_b)

print(f"Test case 2 results : {json.dumps(tcase_2_result, indent = 4)}")