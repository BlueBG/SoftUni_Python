start_number = int(input())
end_number = int(input())

a_1 = (start_number // 1000) % 10
b_1 = (start_number // 100) % 10
c_1 = (start_number // 10) % 10
d_1 = start_number % 10

a_2 = (end_number // 1000) % 10
b_2 = (end_number // 100) % 10
c_2 = (end_number // 10) % 10
d_2 = end_number % 10

for num_1 in range(a_1, a_2 + 1):
    for num_2 in range(b_1, b_2 + 1):
        for num_3 in range(c_1, c_2 + 1):
            for num_4 in range(d_1, d_2 + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")
