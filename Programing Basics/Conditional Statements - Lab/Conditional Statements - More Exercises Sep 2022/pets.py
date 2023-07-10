import math

trip_time = int(input())
food_for_animals_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

dog_food_needed = trip_time * dog_food_kg
cat_food_needed = trip_time * cat_food_kg
turtle_needed_food = (turtle_food_gr / 1000) * trip_time
total_needed_food = dog_food_needed + cat_food_needed + turtle_needed_food
diff = abs(food_for_animals_kg - total_needed_food)
rounded_food = 0

if food_for_animals_kg >= total_needed_food:
    rounded_food = math.floor(diff)
    print(f"{rounded_food} kilos of food left.")
else:
    rounded_food = math.ceil(diff)
    print(f"{rounded_food} more kilos of food are needed.")
