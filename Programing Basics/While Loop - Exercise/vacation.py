needed_money = float(input())
available_money = float(input())

total_money = available_money
count_days = 0
spend_days = 0

while total_money < needed_money:
    if spend_days == 5:
        break
    count_days += 1
    action_name = input()
    spend_save_money = float(input())

    if action_name == "spend":
        total_money -= spend_save_money
        spend_days += 1
        if total_money <= 0:
            total_money = 0

    elif action_name == "save":
        total_money += spend_save_money
        spend_days = 0

if spend_days == 5:
    print("You can't save the money.")
    print(count_days)
else:
    print(f"You saved the money for {count_days} days.")
