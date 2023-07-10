buddget = float(input())
flour_price_per_kg = float(input())

pack_of_eggs_price = flour_price_per_kg * 0.75
milk_price_per_lt = flour_price_per_kg * 1.25

bread_price = pack_of_eggs_price + flour_price_per_kg + (milk_price_per_lt / 4)
bread_count = 0
colored_eggs = 0

while buddget >= bread_price:
    bread_count += 1
    buddget -= bread_price
    colored_eggs += 3


    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {buddget:.2f}BGN left.")
