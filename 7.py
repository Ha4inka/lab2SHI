def split_list(lst):
    unique = []
    duplicates = []
    seen = set()
    for item in lst:
        if lst.count(item) == 1:
            if item not in seen:
                unique.append(item)
        else:
            if item not in seen:
                duplicates.append(item)
        seen.add(item)
    return unique, duplicates

input_list = input("Введіть елементи списку через пробіл: ").split()

unique_list, duplicate_list = split_list(input_list)

print("Унікальні елементи:", " ".join(unique_list))
print("Повторювані елементи:", " ".join(duplicate_list))
