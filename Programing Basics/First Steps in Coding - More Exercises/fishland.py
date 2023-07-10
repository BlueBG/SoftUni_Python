mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

bonito_price = mackerel_price + (mackerel_price * 0.60)
total_bonito_coast = bonito_price * bonito_kg
safrid_price = sprinkle_price + (sprinkle_price * 0.80)
total_safrid_coast = safrid_price * safrid_kg
total_mussels_coast = mussels_kg * 7.50
total_amaunt = total_bonito_coast + total_safrid_coast + total_mussels_coast

print(f"{total_amaunt:.2f}")
