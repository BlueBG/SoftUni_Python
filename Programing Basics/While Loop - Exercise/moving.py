width_room = int(input())
length_room = int(input())
height_room = int(input())

avaleble_space = width_room * length_room * height_room
total_box = 0
moved_box = input()

while moved_box != "Done":
    box_to_store = int(moved_box)
    total_box += box_to_store

    if total_box >= avaleble_space:
        diff = abs(total_box - avaleble_space)
        print(f"No more free space! You need {diff} Cubic meters more.")
        break

    moved_box = input()

diff = abs(total_box - avaleble_space)
if total_box < avaleble_space or moved_box == "Done":
    print(f"{diff} Cubic meters left.")