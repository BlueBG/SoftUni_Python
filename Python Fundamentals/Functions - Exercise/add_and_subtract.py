def add_and_subtrac(a, b, c):
    sum_result = sum_numbers(a, b)
    result = subtrac(sum_result, c)
    return result

def sum_numbers(a, b):
    return a + b

def subtrac (a, b):
    return a - b

first_num = int(input())
second_num = int(input())
third_num = int(input())



print(add_and_subtrac(first_num, second_num, third_num))