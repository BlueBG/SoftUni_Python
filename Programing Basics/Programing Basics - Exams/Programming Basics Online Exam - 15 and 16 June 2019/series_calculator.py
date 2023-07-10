import math

movie_name = input()
season_count = int(input())
episode_count = int(input())
episode_time = float(input())

time_with_comersial = episode_time * 1.20
extra_time = season_count * 10
total_needed_time = math.floor(time_with_comersial * episode_count * season_count + extra_time)
print(f"Total time needed to watch the {movie_name} series is {total_needed_time} minutes.")
