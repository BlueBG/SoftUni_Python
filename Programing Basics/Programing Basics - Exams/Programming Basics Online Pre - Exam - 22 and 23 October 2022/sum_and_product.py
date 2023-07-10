number = int(input())
flag = False
flag_one = False
for a in range(1, 10):
    for b in range(9, a, - 1):
        for c in range(0, 10):
            for d in range(9, c, - 1):
                num = number
                multiplication_numbers = a * b * c * d
                sum_numbers = a + b + c + d
                combination = multiplication_numbers // sum_numbers
                magik = num % 10
                if combination == 3 and magik == 3:
                    print(f"{d}{c}{b}{a}")
                    flag = True
                    break
                elif multiplication_numbers == sum_numbers and magik == 5:
                    flag = True
                    print(f"{a}{b}{c}{d}")
                    break
            if flag:
                break
