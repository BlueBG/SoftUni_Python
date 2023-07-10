city = input()
sale_amaunt = float(input())
bonus = 0
if city == "Sofia":
    if 0 <= sale_amaunt <= 500:
        bonus = sale_amaunt * 0.05
    elif 500 < sale_amaunt <= 1000:
        bonus = sale_amaunt * 0.07
    elif 1000 < sale_amaunt <= 10000:
        bonus = sale_amaunt * 0.08
    elif sale_amaunt > 10000:
        bonus = sale_amaunt * 0.12
elif city == "Varna":
    if 0 <= sale_amaunt <= 500:
        bonus = sale_amaunt * 0.045
    elif 500 < sale_amaunt <= 1000:
        bonus = sale_amaunt * 0.075
    elif 1000 < sale_amaunt <= 10000:
        bonus = sale_amaunt * 0.10
    elif sale_amaunt > 10000:
        bonus = sale_amaunt * 0.13
elif city == "Plovdiv":
    if 0 <= sale_amaunt <= 500:
        bonus = sale_amaunt * 0.055
    elif 500 < sale_amaunt <= 1000:
        bonus = sale_amaunt * 0.08
    elif 1000 < sale_amaunt <= 10000:
        bonus = sale_amaunt * 0.12
    elif sale_amaunt > 10000:
        bonus = sale_amaunt * 0.145
if (city != "Sofia" and city != "Varna" and city != "Plovdiv") or sale_amaunt < 0:
    print("error")
else:
    print(f"{bonus:.2f}")
