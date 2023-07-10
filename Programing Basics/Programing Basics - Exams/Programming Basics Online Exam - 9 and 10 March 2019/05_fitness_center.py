gym_visitors = int(input())

back = 0
chest = 0
legs = 0
abs_workout = 0
protein_shake = 0
protein_bar = 0

for i in range(1, gym_visitors + 1):
    workout_type = input()
    if workout_type == "Back":
        back += 1
    elif workout_type == "Chest":
        chest += 1
    elif workout_type == "Legs":
        legs += 1
    elif workout_type == "Abs":
        abs_workout += 1
    elif workout_type == "Protein shake":
        protein_shake += 1
    elif workout_type == "Protein bar":
        protein_bar += 1

work_out_people = (back + chest + legs + abs_workout) / gym_visitors * 100
protein_people = (protein_bar + protein_shake) / gym_visitors * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_workout} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_people:.2f}% - work out")
print(f"{protein_people:.2f}% - protein")
