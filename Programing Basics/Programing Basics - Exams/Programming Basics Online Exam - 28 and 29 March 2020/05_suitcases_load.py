plane_volume = float(input())
bag_volume = input()

bags_count = 0
total_volume = plane_volume
flag = False
suitcases_loaded = 0
bag_weith = 0
while True:

    if bag_volume == "End":
        break

    bag_weith = float(bag_volume)

    if bags_count == 3:
        bag_weith = bag_weith * 1.10
        bags_count = 0

    total_volume -= bag_weith

    if total_volume < 0:
        flag = True
        break
    bags_count += 1
    suitcases_loaded += 1
    bag_volume = input()

if flag:
    print("No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases_loaded} suitcases loaded.")
