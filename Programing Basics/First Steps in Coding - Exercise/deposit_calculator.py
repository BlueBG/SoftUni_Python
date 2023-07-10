deposit_amount = float(input())
deposit_mounts = int(input())
year_annual = float(input())

annual_count = deposit_amount * (year_annual / 100)
mounth_annual = annual_count / 12
total_money = deposit_amount + deposit_mounts * mounth_annual

print(total_money)
