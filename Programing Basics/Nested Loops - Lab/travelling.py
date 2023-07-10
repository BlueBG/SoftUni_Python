destination = input()
min_budget = input()

total_money = 0

cur_destination = ""
while destination != "End":
    budget = float(min_budget)
    saved_money = float(input())
    total_money += saved_money
    # cur_destination = destination
    if total_money >= budget:
        print(f"Going to {destination}!")
        total_money = 0
        destination = input()
        if destination == "End":
            break
        min_budget = input()

