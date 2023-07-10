import math

people_count = int(input())
enter_tax = float(input())
lounger_price = float(input())
umbrela_price = float(input())


people_for_lounger = math.ceil(people_count * 0.75)
people_for_umbrela = math.ceil(people_count * 0.5)
total_price = (people_count * enter_tax) + (people_for_lounger * lounger_price) + (people_for_umbrela * umbrela_price)
print(f"{total_price:.2f} lv.")
