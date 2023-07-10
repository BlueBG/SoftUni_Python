import math
import sys

easter_bread_count = int(input())

sugar_quantity = 0
flour_quantity = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for i in range(1, easter_bread_count + 1):
    spent_sugar = int(input())
    spent_flour = int(input())
    sugar_quantity += spent_sugar
    flour_quantity += spent_flour
    if spent_sugar > max_sugar:
        max_sugar = spent_sugar
    if spent_flour > max_flour:
        max_flour = spent_flour

sugar_packs = math.ceil(sugar_quantity / 950)
flour_packs = math.ceil(flour_quantity / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
