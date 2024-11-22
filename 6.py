def game():
    n = int(input("Введіть максимально можливе число n: "))
    possible_numbers = set(range(1, n + 1))

    while True:
        question = input("Введіть питання Каті (числа через пробіл або 'Все' для завершення): ")

        if question.strip().lower() == "все":
            break

        question_numbers = set(map(int, question.split()))
        if not question_numbers.issubset(possible_numbers):
            print("Питання містить числа поза діапазоном можливих. Спробуйте ще раз.")
            continue

        if len(question_numbers) * 2 == len(possible_numbers):
            print("Ні")
        else:
            intersection = question_numbers & possible_numbers
            if len(intersection) > len(possible_numbers - intersection):
                print("Так")
                possible_numbers = intersection
            else:
                print("Ні")
                possible_numbers -= question_numbers

    print("Можливі числа Івана:", " ".join(map(str, sorted(possible_numbers))))

game()
