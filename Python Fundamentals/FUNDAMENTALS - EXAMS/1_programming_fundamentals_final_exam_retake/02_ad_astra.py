import re

input_line = input()

total_calories = 0

pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"
food_info = re.finditer(pattern, input_line)

for food in food_info:
    total_calories += int(food["calories"])

total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")

food_info = re.finditer(pattern, input_line)

for food in food_info:
    print(f"Item: {food['item']}, Best before: {food['date']}, Nutrition: {food['calories']}")
