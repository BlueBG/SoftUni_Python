team_name = input()
season_play_count = int(input())

win_count = 0
draw_count = 0
lose_count = 0
points_earned = 0


for game in range(1, season_play_count + 1):
    match_result = input()
    if match_result == "W":
        win_count += 1
        points_earned += 3
    elif match_result == "D":
        draw_count += 1
        points_earned += 1
    elif match_result == "L":
        lose_count += 1


if season_play_count == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_rate = (win_count / season_play_count * 100)
    print(f"{team_name} has won {points_earned} points during this season.")
    print("Total stats:")
    print(f"## W: {win_count}")
    print(f"## D: {draw_count}")
    print(f"## L: {lose_count}")
    print(f"Win rate: {win_rate:.2f}%")
