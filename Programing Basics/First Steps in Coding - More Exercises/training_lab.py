w_meter = float(input())
h_meter = float(input())

corridor_cm = 100
h_room_cm = h_meter * 100 - corridor_cm
h_rows = h_room_cm // 70
w_room_cm = w_meter * 100
w_rows = w_room_cm // 120
seats_caount = h_rows * w_rows - 3

print(seats_caount)
