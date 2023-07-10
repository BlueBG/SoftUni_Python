vegetables_price_kg = float(input())
fruits_price_kg = float(input())
total_vegetables_kg = int(input())
total_fruits_kg = int(input())

vegetables_coast = vegetables_price_kg * total_vegetables_kg
fruits_coast = fruits_price_kg * total_fruits_kg
total_price_in_euro = (vegetables_coast + fruits_coast) / 1.94

print(f"{total_price_in_euro:.2f}")
