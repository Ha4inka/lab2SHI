def game():
    n = int(input())
    possible_n = set(range(1, n + 1))
    while True:
        question = input().strip()
        if question == "Все":
            print(" ".join(map(str, sorted(possible_n))))
            break
        asked_n = set(map(int, question.split()))
        if len(possible_n & asked_n) > len(possible_n) // 2:
            print("Так")
            possible_n &= asked_n
        else:
            print("Ні")
            possible_n -= asked_n


game()
