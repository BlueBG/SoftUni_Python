location_num = int(input())

gold_per_day = 0
days = 0

for location in range(1, location_num + 1):
    expected_avg_gold = float(input())
    days_count = int(input())
    days = days_count
    gold_per_day = 0
    for days in range(1, days_count + 1):
        gold_dig = float(input())
        gold_per_day += gold_dig
    avg_gold = gold_per_day / days
    diff = abs(avg_gold - expected_avg_gold)
    if avg_gold >= expected_avg_gold:
        print(f"Good job! Average gold per day: {avg_gold:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")
