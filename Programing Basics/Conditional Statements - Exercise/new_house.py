flower_type = input()
count_flowers = int(input())
total_budget = int(input())

all_flowers_prise = 0

if flower_type == "Roses":
    all_flowers_prise = count_flowers * 5
    if count_flowers > 80:
        all_flowers_prise = all_flowers_prise * 0.90
elif flower_type == "Dahlias":
    all_flowers_prise = count_flowers * 3.80
    if count_flowers > 90:
        all_flowers_prise = all_flowers_prise * 0.85
elif flower_type == "Tulips":
    all_flowers_prise = count_flowers * 2.80
    if count_flowers > 80:
        all_flowers_prise = all_flowers_prise * 0.85
elif flower_type == "Narcissus":
    all_flowers_prise = count_flowers * 3
    if count_flowers < 120:
        all_flowers_prise = all_flowers_prise * 1.15
elif flower_type == "Gladiolus":
    all_flowers_prise = count_flowers * 2.50
    if count_flowers < 80:
        all_flowers_prise = all_flowers_prise * 1.20

diff = abs(total_budget - all_flowers_prise)

if total_budget >= all_flowers_prise and flower_type in ["Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"]:
    print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {diff:.2f} leva left.")
elif all_flowers_prise > total_budget and flower_type in ["Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"]:
    print(f"Not enough money, you need {diff:.2f} leva more.")
