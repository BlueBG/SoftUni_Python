import sys

player_name = input()

max_goals = -sys.maxsize
goal_count = 0
best_player = ""

while player_name != "END":
    scored_goals = int(input())
    if scored_goals > max_goals:
        max_goals = scored_goals
        best_player = player_name
    if max_goals >= 10:
        break

    player_name = input()
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
