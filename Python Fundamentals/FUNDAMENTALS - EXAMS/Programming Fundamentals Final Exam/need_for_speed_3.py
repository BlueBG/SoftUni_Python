cars_to_buy = int(input())

car_mileage = {}
car_fuel = {}

for i in range(cars_to_buy):
    car_name = input().split('|')
    car_model = car_name[0]
    mileage = int(car_name[1])
    fuel = int(car_name[2])

    car_mileage[car_model] = mileage
    car_fuel[car_model] = fuel

while True:
    command_arc = input()

    if command_arc == "Stop":
        break
    command_line = command_arc.split(' : ')
    # command_line = input().split(':')
    command = command_line[0]
    car = command_line[1]

    if command == "Drive":
        distance = int(command_line[2])
        fuel = int(command_line[3])

        if car_fuel[car] < fuel:
            print(f"Not enough fuel to make that ride")

        else:
            car_mileage[car] += distance
            car_fuel[car] -= fuel

            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if car_mileage[car] >= 100000:
                car_mileage.pop(car)
                print(f"Time to sell the {car}!")

            # else:
            #     print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    elif command == "Refuel":
        fuel = int(command_line[2])
        refuel = 0

        if car_fuel[car] + fuel > 75:
            refuel = 75 - car_fuel[car]
            car_fuel[car] = 75

        else:
            car_fuel[car] += fuel
            refuel = fuel

        print(f"{car} refueled with {refuel} liters")

    elif command == "Revert":
        mileage_decreased = int(command_line[2])
        car_mileage[car] -= mileage_decreased
        if int(car_mileage[car]) < 10000:
            car_mileage[car] = 10000
            continue


        else:
            print(f"{car} mileage decreased by {mileage_decreased} kilometers")

for car in car_fuel.keys():
    fuel = car_fuel[car]
    mileage = car_mileage[car]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

             # 80 POINTS