number = int(input())

for thousand in range(1, 10):
    for hundred in range(1, 10):
        for ten in range(1, 10):
            for units in range(1, 10):
                if number % thousand == 0 and number % hundred == 0 and number % ten == 0 and number % units == 0:
                    print(f"{thousand}{hundred}{ten}{units}", end=" ")
