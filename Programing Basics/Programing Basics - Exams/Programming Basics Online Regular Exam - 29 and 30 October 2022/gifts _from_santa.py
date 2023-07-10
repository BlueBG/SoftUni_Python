n = int(input())
m = int(input())
s = int(input())

for numbers in range(m, n-1, -1):
    if numbers % 2 == 0 and numbers % 3 == 0:
        if s == numbers:
            break
        print(f"{numbers}", end=" ")
