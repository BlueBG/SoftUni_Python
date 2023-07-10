fruit = input()
day_of_week = input()
quantity = float(input())

total_price = 0
flag = True

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        total_price = quantity * 2.50
    elif fruit == "apple":
        total_price = quantity * 1.20
    elif fruit == "orange":
        total_price = quantity * 0.85
    elif fruit == "grapefruit":
        total_price = quantity * 1.45
    elif fruit == "kiwi":
        total_price = quantity * 2.70
    elif fruit == "pineapple":
        total_price = quantity * 5.50
    elif fruit == "grapes":
        total_price = quantity * 3.85
    else:
        flag = False

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        total_price = quantity * 2.70
    elif fruit == "apple":
        total_price = quantity * 1.25
    elif fruit == "orange":
        total_price = quantity * 0.90
    elif fruit == "grapefruit":
        total_price = quantity * 1.60
    elif fruit == "kiwi":
        total_price = quantity * 3
    elif fruit == "pineapple":
        total_price = quantity * 5.60
    elif fruit == "grapes":
        total_price = quantity * 4.20
    else:
        flag = False
if total_price != 0 and flag:
    print(f"{total_price:.2f}")
else:
    print("error")