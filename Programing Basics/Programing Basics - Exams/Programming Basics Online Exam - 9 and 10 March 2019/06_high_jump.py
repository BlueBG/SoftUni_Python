wonted_high_cm = int(input())

failed_attempts = 0
curent_jump = 0
jump_counter = 0
curent_high = wonted_high_cm - 30
flag = False

while curent_jump < wonted_high_cm:
    jump_high == curent_jump
    jump_high = int(input())

    if jump_high > curent_high:

        jump_counter += 1
        failed_attempts = 0
        curent_high += 5

    elif jump_high <= curent_high:
        failed_attempts += 1

        jump_counter += 1

    if failed_attempts == 3:
        flag = True
        break


if flag:
    print(f"Tihomir failed at {curent_jump}cm after {jump_counter} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {wonted_high_cm}cm after {jump_counter} jumps.")
