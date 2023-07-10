length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
accessories_percent = float(input())

aquarium_total_volume = length_cm * width_cm * height_cm
aquarium_total_volume_liters = aquarium_total_volume / 1000
occupied_space = accessories_percent / 100
needed_wather_littres = aquarium_total_volume_liters * (1 - occupied_space)

print(needed_wather_littres)