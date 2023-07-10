import math

tournament_count = int(input())
starting_points = int(input())

points = 0
total_wins = 0

for i in range(1, tournament_count + 1):
    tournament_stage = input()

    if tournament_stage == "W":
        total_wins += 1
        points += 2000
    elif tournament_stage == "F":
        points += 1200
    elif tournament_stage == "SF":
        points += 720

total_points = points + starting_points
avg_points = math.floor(points / tournament_count)
win_percent = (total_wins / tournament_count) * 100

print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{win_percent:.2f}%")
