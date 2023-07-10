import sys

easter_bread_count = int(input())

total_points = 0
baker_name = ""
max_pts = -sys.maxsize
max_pts_name = ""
count_pts = 0

for i in range(1, easter_bread_count + 1):
    print(f"{max_pts_name} is the new number 1!")

    name = input()
    grade_per_person = input()
    total_points = 0
    while grade_per_person != "Stop":
        # if grade_per_person == "Stop":
        #     break
        person_grade = int(grade_per_person)
        total_points += person_grade
        baker_name = name
        grade_per_person = input()
    if max_pts < total_points:
        max_pts = total_points
        max_pts_name = baker_name
    print(f"{name} has {total_points} points.")

print(f"{max_pts_name} won competition with {max_pts} points!")
