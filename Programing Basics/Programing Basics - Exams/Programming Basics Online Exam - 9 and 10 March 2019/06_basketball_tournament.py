game_number = 0
home_wins = 0
visitor_wins = 0
total_played_games = 0
wins_percent = 0
lost_percent = 0
flag = False
tournament_name = input()
tournament_games = int(input())

while tournament_name != "End of tournaments":
    game_number = 0

    for i in range(1, tournament_games + 1):
        home_team_score = int(input())
        visitor_team_score = int(input())
        total_played_games += 1
        diff = abs(home_team_score - visitor_team_score)

        if home_team_score > visitor_team_score:
            home_wins += 1
            game_number += 1
            print(f"Game {game_number} of tournament {tournament_name}: win with {diff} points.")

        elif home_team_score < visitor_team_score:
            visitor_wins += 1
            game_number += 1
            print(f"Game {game_number} of tournament {tournament_name}: lost with {diff} points.")
    tournament_name = input()
    if tournament_name == "End of tournaments":
        flag = True
        break
    tournament_games = int(input())

if flag:
    wins_percent = (home_wins / total_played_games) * 100
    lost_percent = (visitor_wins / total_played_games) * 100
    print(f"{wins_percent:.2f}% matches win")
    print(f"{lost_percent:.2f}% matches lost")
