coffies_needed = 0

while True:
    command = input()
    if command == "END":
        break

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffies_needed += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffies_needed += 2

if coffies_needed > 5:
    print("You need extra sleep")
else:
    print(coffies_needed)
