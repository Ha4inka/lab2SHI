def extract_negatives_manual(lst):
    result = []
    for num in lst:
        if num < 0:
            result.append(num)
    return result

print(extract_negatives_manual([1, -5, 7, -3, 0]))

def extract_negatives_generator(lst):
    return [num for num in lst if num < 0]

print(extract_negatives_generator([1, -5, 7, -3, 0]))
