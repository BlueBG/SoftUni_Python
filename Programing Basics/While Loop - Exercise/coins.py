money_change = float(input())

coins = 0
change_coins = money_change * 100

while change_coins > 0:
    if change_coins >= 200:
        change_coins -= 200
        coins += 1
    elif change_coins >= 100:
        change_coins -= 100
        coins += 1
    elif change_coins >= 50:
        change_coins -= 50
        coins += 1
    elif change_coins >= 20:
        change_coins -= 20
        coins += 1
    elif change_coins >= 10:
        change_coins -= 10
        coins += 1
    elif change_coins >= 5:
        change_coins -= 5
        coins += 1
    elif change_coins >= 2:
        change_coins -= 2
        coins += 1
    elif change_coins >= 1:
        change_coins -= 1
        coins += 1
    else:
        break
print(coins)

