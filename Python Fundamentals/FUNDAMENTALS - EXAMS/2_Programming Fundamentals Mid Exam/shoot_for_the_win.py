# sequence_of_integers = input().split()
targets_and_value = [int(x) for x in input().split()]

list_of_targets = []

while True:
    command_line = input()

    if command_line == "End":
        break

    target_index = int(command_line)

    if list_of_targets[target_index] != -1:
        target_index = -1
print(list_of_targets)