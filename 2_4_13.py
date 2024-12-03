def insert_number(lst, index, number):
    return lst[:index] + [number] + lst[index:]

print(insert_number([1, 2, 3], 1, 10))
