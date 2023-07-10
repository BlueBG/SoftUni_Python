budget = float(input())
ticket_type = input()
people_count = int(input())

transport_price = 0
t_price = 0

if people_count < 5:
    transport_price = budget * 0.75
elif people_count < 10:
    transport_price = budget * 0.60
elif people_count < 25:
    transport_price = budget * 0.50
elif people_count < 50:
    transport_price = budget * 0.40
else:
    transport_price = budget * 0.25

if ticket_type == "Normal":
    t_price = 249.99
elif ticket_type == "VIP":
    t_price = 499.99
total_price = transport_price + (people_count * t_price)
diff = abs(budget - total_price)

if total_price <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")