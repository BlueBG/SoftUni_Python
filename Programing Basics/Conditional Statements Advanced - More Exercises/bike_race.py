junior_bikers = int(input())
senior_biker = int(input())
track_type = input()

all_bikers = junior_bikers + senior_biker
total = 0

if track_type == "trail":
    total = (junior_bikers * 5.50) + (senior_biker * 7)
elif track_type == "cross-country":
    total = (junior_bikers * 8) + (senior_biker * 9.50)
elif track_type == "downhill":
    total = (junior_bikers * 12.25) + (senior_biker * 13.75)
elif track_type == "road":
    total = (junior_bikers * 20) + (senior_biker * 21.50)

if all_bikers >= 50 and track_type == "cross-country":
    total = (total * 0.75) * 0.95
else:
    total = total * 0.95

print(f"{total:.2f}")
