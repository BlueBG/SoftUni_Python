initial_energy = int(input())

games_win = 0

while True:
    enemy_distance = input()

    if enemy_distance == "End of battle":
        break

    initial_energy -= int(enemy_distance)
    games_win += 1

    if initial_energy < 0 or initial_energy < int(enemy_distance):
        print(f"Not enough energy! Game ends with {games_win} won battles and {initial_energy} energy")
        exit()


    elif games_win % 3 == 0:
        initial_energy += games_win

print(f"Won battles: {games_win}. Energy left: {initial_energy}" )