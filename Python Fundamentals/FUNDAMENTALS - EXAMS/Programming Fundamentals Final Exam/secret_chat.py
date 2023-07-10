message = input()
while True:
    command_line = input().split(':|:')
    command = command_line[0]

    if command == "Reveal":
        break

    if command == "InsertSpace":
        index = int(command_line[1])
        message = message[:index] + ' ' + message[index:]

    elif command == "Reverse":
        subs_str_to_reverce = command_line[1]
        if message.find(subs_str_to_reverce) != -1:
            message = message.replace(subs_str_to_reverce, '')
            subs_str_to_reverce = subs_str_to_reverce[::-1]
            message += subs_str_to_reverce


        else:
            print("error")
            continue

    elif command == "ChangeAll":
        old_string = command_line[1]
        new_string = command_line[2]
        message = message.replace(old_string, new_string)

    print(message)

print(f"You have a new text message: {message}")

                # """ 87 POINTS EARNED"""
