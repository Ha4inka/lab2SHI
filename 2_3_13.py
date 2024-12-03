def remove_number_manual(lst, n):
    result = []
    for num in lst:
        if num != n:
            result.append(num)
    return result

print(remove_number_manual([1, 2, 3, 2, 4], 2))

def remove_number_generator(lst, n):
    return [num for num in lst if num != n]

print(remove_number_generator([1, 2, 3, 2, 4], 2))
