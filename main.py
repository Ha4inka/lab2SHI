import random

def fill_list_manual(p, a, b):
    result = []
    for _ in range(p):
        result.append(random.randint(a, b))
    return result

print(fill_list_manual(5, -10, 10))
