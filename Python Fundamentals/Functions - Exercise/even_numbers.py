def is_even(number):
    result = number % 2 == 0
    return result

# numbers = input().split()
nums = [int(num) for num in input().split()]

print(list(filter(is_even, nums)))