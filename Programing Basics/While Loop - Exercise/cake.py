width_cake = int(input())
length_cake = int(input())

pieces = 0
all_pieces = 0
needed_peaces = input()
flag = False
while needed_peaces != "STOP":
    need_pieace = int(needed_peaces)
    all_pieces = width_cake * length_cake
    pieces += need_pieace

    if pieces > all_pieces:
        diff = abs(pieces - all_pieces)
        print(f"No more cake left! You need {diff} pieces more.")
        break

    needed_peaces = input()

diff = abs(pieces - all_pieces)
if all_pieces >= pieces or needed_peaces == "STOP":
    print(f"{diff} pieces are left.")
