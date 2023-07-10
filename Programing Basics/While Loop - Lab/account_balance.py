deposit_money = input()

account_balance = 0
flag = True
while deposit_money != "NoMoreMoney":
    deposit_money = float(deposit_money)
    if deposit_money < 0:
        flag = False
        print("Invalid operation!")
        print(f"Total: {account_balance:.2f}")
        break
    account_balance += deposit_money
    print(f"Increase: {deposit_money:.2f}")
    deposit_money = input()

if flag:
    print(f"Total: {account_balance:.2f}")
