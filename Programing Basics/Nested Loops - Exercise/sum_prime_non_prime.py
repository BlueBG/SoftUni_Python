number = input()

sum_prime = 0
sum_non_prime = 0
counter = 0

while number != "stop":
    num = int(number)

    if num < 0:
        print("Number is negative.")
        number = input()
        continue
    counter = 0
    for n in range(1, num + 1):
        if num % n == 0:
            counter += 1

    if counter == 2:
        sum_prime += num
    else:
        sum_non_prime += num

    number = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
