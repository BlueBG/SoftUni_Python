
array_values = input().split()


int_list = [eval(i) for i in array_values]

while True:
    command_line = input().split()
    if "end" in command_line:
        break
    elif "decrease" in command_line:
        for i in range(len(int_list)):
            int_list[i] -= 1
        continue

    command = command_line[0]
    first_number = int(command_line[1])
    second_number = int(command_line[2])

    if command == "swap":
        int_list[first_number], int_list[second_number] = int_list[second_number], int_list[first_number]
    elif command == "multiply":
        int_list[first_number] = int_list[first_number] * int_list[second_number]

int_list = [str(x) for x in int_list]
print(', '.join(int_list))