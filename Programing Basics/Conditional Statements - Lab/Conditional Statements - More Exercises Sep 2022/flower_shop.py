import math

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cactus_price = 8
flowers_price = (magnolias_price * magnolias_count) + (hyacinths_price * hyacinths_count) + (roses_price * roses_count) \
             + (cactus_count * cactus_price)
total_price = flowers_price * 0.95
diff = abs( present_price - total_price)

if present_price > total_price:
    diff = math.ceil(diff)
    print(f"She will have to borrow {diff} leva.")
else:
    diff = math.floor(diff)
    print(f"She is left with {diff} leva.")
