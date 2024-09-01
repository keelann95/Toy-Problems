def merge_dicts(dict1, dict2):
    merged = dict(dict1)
    
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value

    return merged
# example
dict_a = {'a': 9, 'b': 24}
dict_b = {'b': 6, 'c': 94}

merged_dict = merge_dicts(dict_a, dict_b)
print(merged_dict)