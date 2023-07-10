distance_amaunt = int(input())
daytime = input()

total_price = 0
total_taxi_price = 0

if distance_amaunt >= 100:
    total_price = distance_amaunt * 0.06
elif distance_amaunt >= 20:
    total_price = distance_amaunt * 0.09
if daytime == "day":
    total_taxi_price = (distance_amaunt * 0.79) + 0.70
elif daytime == "night":
    total_taxi_price = (distance_amaunt * 0.90) + 0.7
if total_price > total_taxi_price or total_price == 0:
    print(f"{total_taxi_price:.2f}")
else:
    print(f"{total_price:.2f}")
