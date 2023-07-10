family_budget = float(input())
nights_count = int(input())
night_price = float(input())
expense_percent = int(input())

discount = 0
expense_amaunt = family_budget * (expense_percent / 100)
total_price = 0
if nights_count > 7:
    discount = night_price * 0.05
    total_price = (night_price - discount) * nights_count + expense_amaunt
elif nights_count <= 7:
        total_price = night_price * nights_count + expense_amaunt
diff = abs(family_budget - total_price)

if family_budget >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")