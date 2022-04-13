def frequency(lst):
    frequency_map = dict()
    # Map numbers in lst to frequency dictionary (number <-> frequency)
    for item in lst:
        if item not in frequency_map.keys():
            frequency_map[item] = 1
        else:
            frequency_map[item] += 1

    # frequency <-> [numbers...] mapping
    reverse_frequency_map = dict()
    frequency_map_keys = frequency_map.keys()

    # Get first key
    frequency_map_key_list = list(frequency_map_keys)
    first_key = frequency_map_key_list[0]

    # Assume min and max frequencies
    min_freq = frequency_map[first_key]
    max_freq = 0
    for key in frequency_map.keys():
        value = frequency_map[key]
        # Determine min and max frequency values
        if value < min_freq:
            min_freq = value
        if value > max_freq:
            max_freq = value

        # Reverse frequency map (from number <-> frequency to frequency <-> [numbers...])
        if value not in reverse_frequency_map.keys():
            reverse_frequency_map[value] = [key]
        else:
            reverse_frequency_map[value].append(key)

    # Get numbers with min frequency
    min_freq_list = reverse_frequency_map[min_freq]
    max_freq_list = reverse_frequency_map[max_freq]

    return min_freq_list, max_freq_list


input_list = list()
for i in range(10):
    try:
        inp = int(input("Enter a number : "))
        input_list.append(inp)
    except:
        i -= 1

min_list, max_list = frequency(input_list)
print(f"Numbers with min frequency : {min_list}")
print(f"Numbers with max frequency : {max_list}")