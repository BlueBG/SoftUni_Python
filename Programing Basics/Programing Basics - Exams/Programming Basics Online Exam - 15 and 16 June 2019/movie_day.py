shote_time = int(input())
scene_count = int(input())
time_for_scene = int(input())

prepare_time = shote_time * 0.15
need_time = scene_count * time_for_scene + prepare_time
diff = abs(shote_time - need_time)
rounded_diff = round(diff)

if shote_time < need_time:
    print(f"Time is up! To complete the movie you need {rounded_diff} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {rounded_diff} minutes left!")
