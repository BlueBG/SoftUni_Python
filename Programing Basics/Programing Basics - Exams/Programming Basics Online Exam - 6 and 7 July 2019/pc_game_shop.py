sold_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0
total_sold_games = 0

for i in range(1, sold_games + 1):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    elif game_name != "Hearthstone" and game_name != "Fornite" and game_name != "Overwatch":
        others += 1
    total_sold_games += 1


print(f"Hearthstone - {hearthstone / total_sold_games * 100:.2f}%")
print(f"Fornite - {fornite / total_sold_games * 100:.2f}%")
print(f"Overwatch - {overwatch / total_sold_games * 100:.2f}%")
print(f"Others - {others / total_sold_games * 100:.2f}%")
