joury_num = int(input())
presentation_name = input()

avg_presentation_garde = 0
sum_grade = 0
total_grade = 0
joury_count = 0

while presentation_name != "Finish":
    sum_grade = 0

    for i in range(1, joury_num + 1):
        grade = float(input())
        total_grade += grade
        sum_grade += grade
        avg_presentation_garde = sum_grade / joury_num
        joury_count += 1

    print(f"{presentation_name} - {avg_presentation_garde:.2f}.")
    presentation_name = input()
total_avg_grade = total_grade / joury_count
print(f"Student's final assessment is {total_avg_grade:.2f}.")
