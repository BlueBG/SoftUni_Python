cards = input().split()

a_team_sent_off_list = []
b_team_sent_off_list = []

game_terminated = False

for card in cards:

    if card in a_team_sent_off_list or card in b_team_sent_off_list:
        continue

    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == "A"

    if is_first_team:
        a_team_sent_off_list.append(card)
    else:
        b_team_sent_off_list.append(card)

    if len(a_team_sent_off_list) > 4 or len(a_team_sent_off_list) > 4:
        game_terminated = True
        break

starting_team_player_count = 11
a_team_final_players_count = starting_team_player_count - len(a_team_sent_off_list)
b_team_final_players_count = starting_team_player_count - len(b_team_sent_off_list)

print(f"Team A - {a_team_final_players_count}; Team B - {b_team_final_players_count}")
if game_terminated:
    print(f"Game was terminated")
