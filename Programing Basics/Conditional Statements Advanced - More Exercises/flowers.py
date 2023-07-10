chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day_type = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
flowers_count = chrysanthemums + roses + tulips
total_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemums * 2
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50
    total_price = roses_price + chrysanthemums_price + tulips_price
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15
    total_price = roses_price + chrysanthemums_price + tulips_price

if day_type == "Y":
    total_price = total_price * 1.15

if tulips > 7 and season == "Spring":
    total_price = total_price * 0.95
elif roses >= 10 and season == "Winter":
    total_price = total_price * 0.90
if flowers_count > 20:
    total_price = total_price * 0.80
total_price += 2
print(f"{total_price:.2f}")
