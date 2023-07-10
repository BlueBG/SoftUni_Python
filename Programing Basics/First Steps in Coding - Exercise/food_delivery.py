chiken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chiken_menu_coast = chiken_menu * 10.35
fish_menu_coast = fish_menu * 12.40
vegan_menu_coast = vegan_menu * 8.15
all_menu_coast = chiken_menu_coast + fish_menu_coast + vegan_menu_coast
dessert_coast = all_menu_coast * 0.2
total_price = all_menu_coast + dessert_coast + 2.50

print(total_price)
