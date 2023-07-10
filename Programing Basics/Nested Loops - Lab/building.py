floors_count = int(input())
flats_per_floor = int(input())

apartment_type = ""

for floor in range(floors_count, 0, - 1):
    for a in range(flats_per_floor):

        if floor == floors_count:
            apartment_type = f"L{floor}{a}"

        elif floor % 2 == 0:
            apartment_type = f"O{floor}{a}"

        elif floor % 2 != 0:
            apartment_type = f"A{floor}{a}"

        print(apartment_type, end=' ')
    print()
