comand_line = int(input())
word_for_filter = input()

cours_names = []
filtered_courses = []

for i in range(comand_line):
    cours_name = input()
    cours_names.append(cours_name)

    if word_for_filter in cours_name:
        filtered_courses.append(cours_name)

print(cours_names)
print(filtered_courses)