first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())

student_left = student_count
student_per_hour = first_employee + second_employee + third_employee
needed_time = 0

while True:
    if student_count == 0:
        break
    student_left -= student_per_hour
    needed_time += 1

    if needed_time % 4 == 0:
        student_left += student_per_hour
        continue

    if student_left <= 0:
        break

print(f"Time needed: {needed_time}h.")
