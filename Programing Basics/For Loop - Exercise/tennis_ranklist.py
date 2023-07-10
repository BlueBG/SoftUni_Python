import math

tournaments = int(input())
start_point = int(input())

wins = 0
finals = 0
semi_finals = 0
tour_points = 0


for i in range(1, tournaments + 1):
    tour_ranking = input()

    if tour_ranking == "W":
        tour_points += 2000
        wins += 1
    elif tour_ranking == "F":
        tour_points += 1200
        finals += 1
    elif tour_ranking == "SF":
        tour_points += 720
        semi_finals += 1

total_point = tour_points + start_point
average_points = math.floor(tour_points / tournaments)
tour_percent = (wins / tournaments) * 100

print(f"Final points: {total_point}")
print(f"Average points: {average_points}")
print(f"{tour_percent:.2f}%")

