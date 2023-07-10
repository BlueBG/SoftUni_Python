start_number = int(input())
end_number = int(input())
magik_number = int(input())

number_of_combinations = 0
a = 0
b = 0
num_result = 0
flag = False

for a in range(start_number, end_number + 1):
    for b in range(start_number, end_number + 1):
        number_of_combinations += 1

        if a + b == magik_number:
            print(f"Combination N:{number_of_combinations} ({a} + {b} = {magik_number})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{number_of_combinations} combinations - neither equals {magik_number}")