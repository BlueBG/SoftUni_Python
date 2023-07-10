numbers_of_iteration = int(input())

flag = False

for i in range(numbers_of_iteration):
    number = int(input())

    if number % 2 != 0:
        flag = False
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")