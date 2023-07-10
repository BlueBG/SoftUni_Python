rest_days = int(input())

work_days = 365 - rest_days
total_play_time = (work_days * 63) + (rest_days * 127)
diff = abs(total_play_time - 30000)
hours_play = diff // 60
minutes_play = diff % 60

if total_play_time > 30000:
    print("Tom will run away")
    print(f"{hours_play} hours and {minutes_play} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_play} hours and {minutes_play} minutes less for play")
