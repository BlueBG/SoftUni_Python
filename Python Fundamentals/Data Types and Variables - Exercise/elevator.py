import math

num_peoples = int(input())
elevator_capacity = int(input())

course_count = math.ceil(num_peoples / elevator_capacity)

print(course_count)

