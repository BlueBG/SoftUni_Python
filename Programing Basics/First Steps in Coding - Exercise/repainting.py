nylon_need_square_meter = int(input())
paint_need = int(input())
thinner_liters = int(input())
time_for_finish = int(input())

nylon_price = (nylon_need_square_meter + 2) * 1.50
paint_price = (paint_need +(paint_need / 10)) * 14.50
thinner_price = thinner_liters * 5
nylon_bags = 0.40
material_coast = nylon_price + paint_price + thinner_price + nylon_bags
worker_coast = (material_coast * 0.30) * time_for_finish

total_amaunt = worker_coast + material_coast

print(total_amaunt)

