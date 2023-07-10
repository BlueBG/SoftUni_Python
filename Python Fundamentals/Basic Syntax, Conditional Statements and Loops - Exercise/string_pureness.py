number_of_strings = int(input())

for _ in range(number_of_strings):
    string = input()

    flag = True
    for ch in string:
        if ch == "," or ch == "." or ch == "_":
            flag = False
            break

    if flag:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")