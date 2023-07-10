budget = int(input())
command = input()

money_spend = 0

while command != "End":
    price = int(command)
    money_spend += price

    if money_spend > budget:
        print(f"You went in overdraft!")
        break
    command = input()

else:
    print(f"You bought everything needed.")