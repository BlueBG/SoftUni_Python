fats_percent = int(input())
protein_percent = int(input())
carbohydrates_percent = int(input())
total_calories = int(input())
wather_percent = int(input())

fats_gram = ((total_calories * fats_percent) / 100) / 9
protein_gram = ((total_calories * protein_percent) / 100) / 4
carbohydrates_gram = ((total_calories * carbohydrates_percent) / 100) / 4
total_food = fats_gram + protein_gram + carbohydrates_gram
calories_per_gram = total_calories / total_food
percent_without_wather = 100 - wather_percent
caloris = (calories_per_gram * percent_without_wather) / 100
print(f"{caloris:.4f}")
