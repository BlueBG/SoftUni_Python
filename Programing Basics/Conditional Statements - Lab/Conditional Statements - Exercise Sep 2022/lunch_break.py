import math

movie_name = input()
movie_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4
movie_time_left = (break_duration - lunch_time - relax_time)
diff = abs(movie_time_left - movie_duration)
rounded_diff = math.ceil(diff)
if movie_time_left >= movie_duration:
    print(f"You have enough time to watch {movie_name} and left with {rounded_diff} minutes free time.")
elif movie_duration > movie_time_left:
    print(f"You don't have enough time to watch {movie_name}, you need {rounded_diff} more minutes.")
