def expanding(parameter_list):
    last_diff = 0
    for idx in range(len(parameter_list) - 1):
        current, next = parameter_list[idx], parameter_list[idx + 1]
        current_diff = abs(next - current)
        if current_diff <= last_diff:
            return False
        else:
            last_diff = current_diff
    return True


test_cases = [
    [1, 3, 7, 2, 9],
    [1, 3, 7, 2, -3],
    [1, 3, 7, 10]
]

for test_case in test_cases:
    print(f"{test_case} : {expanding(test_case)}")