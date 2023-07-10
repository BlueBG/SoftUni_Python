number = int(input())

combination_caunt = 0

for a in range(0, number + 1):
    for b in range(0, number + 1):
        for c in range(0, number + 1):
            result = a + b + c
            if result == number:
                combination_caunt += 1
print(combination_caunt)
