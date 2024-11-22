groups = {
    "Група 1": {"кількість студентів": 25, "староста": "Іванов І.І."},
    "Група 2": {"кількість студентів": 20, "староста": "Петров П.П."},
}


def show_student_count(group_name):
    return groups[group_name]["кількість студентів"]


def show_leader(group_name):
    return groups[group_name]["староста"]


def groups_with_max_students(limit):
    return tuple(group for group, data in groups.items() if data["кількість студентів"] <= limit)


def groups_with_min_students(limit):
    return tuple(group for group, data in groups.items() if data["кількість студентів"] >= limit)


def change_student_count(group_name, new_count):
    groups[group_name]["кількість студентів"] = new_count


def change_leader(group_name, new_leader):
    groups[group_name]["староста"] = new_leader


def add_group(group_name, count, leader):
    groups[group_name] = {"кількість студентів": count, "староста": leader}


def remove_group(group_name):
    groups.pop(group_name, None)


def get_leader_set():
    return set(data["староста"] for data in groups.values())


def menu():
    while True:
        print("\nМеню:")
        print("1. Кількість студентів у групі")
        print("2. ПІБ старости")
        print("3. Групи з кількістю студентів ≤ значення")
        print("4. Групи з кількістю студентів ≥ значення")
        print("5. Змінити кількість студентів")
        print("6. Змінити ПІБ старости")
        print("7. Додати групу")
        print("8. Видалити групу")
        print("9. Показати старост")
        print("0. Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            group = input("Введіть назву групи: ")
            print(f"Кількість студентів: {show_student_count(group)}")
        elif choice == "2":
            group = input("Введіть назву групи: ")
            print(f"Староста: {show_leader(group)}")
        elif choice == "3":
            limit = int(input("Введіть максимальну кількість студентів: "))
            print(f"Групи: {groups_with_max_students(limit)}")
        elif choice == "4":
            limit = int(input("Введіть мінімальну кількість студентів: "))
            print(f"Групи: {groups_with_min_students(limit)}")
        elif choice == "5":
            group = input("Введіть назву групи: ")
            count = int(input("Введіть нову кількість студентів: "))
            change_student_count(group, count)
        elif choice == "6":
            group = input("Введіть назву групи: ")
            leader = input("Введіть нове ПІБ старости: ")
            change_leader(group, leader)
        elif choice == "7":
            group = input("Введіть назву групи: ")
            count = int(input("Введіть кількість студентів: "))
            leader = input("Введіть ПІБ старости: ")
            add_group(group, count, leader)
        elif choice == "8":
            group = input("Введіть назву групи: ")
            remove_group(group)
        elif choice == "9":
            print(f"Старости: {get_leader_set()}")
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


menu()
