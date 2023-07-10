message = input()

while True:

    command_line = input().split("|")
    command = command_line[0]

    if command == "Decode":
        break

    if command == "Move":
        letters_num = int(command_line[1])
        letters_to_move = message[:letters_num]
        message = message[letters_num:] + letters_to_move

    elif command == "Insert":
        idx = int(command_line[1])
        value = command_line[2]
        message = message[0:idx] + value + message[idx:]
    elif command == "ChangeAll":
        substring = command_line[1]
        replacement = command_line[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
