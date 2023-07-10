food = int(input())
dog_eat_per_meal = input()

food_grams = food * 1000
sum_food = 0
while dog_eat_per_meal != "Adopted":

    dog_eat = int(dog_eat_per_meal)
    sum_food += dog_eat
    dog_eat_per_meal = input()

diff = abs(sum_food - food_grams)

if sum_food <= food_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
