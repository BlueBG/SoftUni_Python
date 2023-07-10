import math

world_record = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

distance_time = distance_in_meters * time_per_meter
distance_time_delay = math.floor(distance_in_meters / 15) * 12.50
total_time = distance_time + distance_time_delay

diff = abs(world_record - total_time)

if world_record <= total_time:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:

    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
