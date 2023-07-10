hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60
all_time_minutes = time_in_minutes + minutes + 15

total_hour = all_time_minutes // 60
total_minutes = all_time_minutes % 60

if total_hour > 23:
    total_hour = 0

if total_minutes < 10:
    print(f"{total_hour}:0{total_minutes}")
else:
    print(f"{total_hour}:{total_minutes}")
