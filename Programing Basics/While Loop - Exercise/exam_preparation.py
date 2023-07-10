max_poor_grade = int(input())

counter = 0
total_grade = 0
poor_grade = 0
last_problem_name = 0
flag = False

task_name = input()

while task_name != "Enough":
    task_grade = int(input())
    last_problem_name = task_name
    counter += 1
    total_grade += task_grade
    if task_grade <= 4:
        poor_grade += 1
        if poor_grade == max_poor_grade:
            flag = True
            break
    task_name = input()

avg_grade = total_grade / counter

if flag:
    print(f"You need a break, {poor_grade} poor grades.")

else:
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {counter}")
    print(f"Last problem: {last_problem_name}")
