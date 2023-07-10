numbers = [int(x) for x in input().split()]
count_to_remove = int(input())


for num in range(count_to_remove):
    min_numbers = min(numbers)
    numbers.remove(min_numbers)

print(", ".join([str(x) for x in numbers]))


