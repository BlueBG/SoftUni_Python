actor_name = input()
starting_points = float(input())
people_count = int(input())

all_name_points = 0
total_point = 0
for i in range(people_count):
    name = input()
    points = float(input())
    name_points = (len(name) * points) / 2
    all_name_points += name_points
    total_point = all_name_points + starting_points
    if total_point > 1250.5:
        break

if total_point < 1250.5:
    diff = 1250.5 - total_point
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
elif total_point > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_point:.1f}!")
