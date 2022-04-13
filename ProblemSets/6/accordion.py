def accordion(parameter_list: list) -> bool:
    """
    :param parameter_list: List containing integers
    :return: True if difference alternates, else False
    """
    list_len =  len(parameter_list)
    last_diff = 0
    if list_len < 3:
        print("Please provide a list with 3 or more elements!")
        exit(0)
    diff_flag = 0
    """
    diff_flag == 0 : Decreasing
    diff_flag == 1 : Increasing
    """

    """
    Lines 16 - 23 : Determine starting flag value, whether to follow Decrease-Increase-Decrease or Increase-Decrease-Increase
    """
    first_diff = abs(parameter_list[0] - parameter_list[1])
    second_diff = abs(parameter_list[1] - parameter_list[2])
    if first_diff < second_diff:
        diff_flag = 0
    elif first_diff > second_diff:
        diff_flag = 1
    else:
        """
        Difference is neutral (neither greater nor lesser), hence terminate
        """
        return False

    last_diff = second_diff

    """
    Difference finding logic, based on parameters deduced above
    """
    for idx in range(2, list_len - 1):
        current, next = parameter_list[idx], parameter_list[idx + 1]
        current_diff = abs(current - next)
        if diff_flag == 1:
            """
            If ascending
            """
            if current_diff <= last_diff:
                return False
            else:
                diff_flag = 0
                last_diff = current_diff
        else:
            """
            If descending
            """

            if current_diff >= last_diff:
                return False
            else:
                diff_flag = 1
                last_diff = current_diff

    return True


test_cases = [
    [1, 5, 1],
    [1, 5, 2, 8, 3],
    [-2, 1, 5, 2, 8, 3],
    [1, 5, 2, 8, 1]
]

for test_case in test_cases:
    print(f"{test_case} : {accordion(test_case)}")

userInputList = list()
while True:
    userInput = input("Enter list element or enter 'exit' to stop : ")
    if userInput == 'exit':
        break
    userInputList.append(int(userInput))
print(f"{userInputList} : {accordion(userInputList)}")

