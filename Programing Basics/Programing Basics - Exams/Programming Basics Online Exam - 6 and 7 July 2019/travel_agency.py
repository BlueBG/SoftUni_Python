city_name = input()
pack_type = input()
vip_card = input()
stay_days = int(input())

price = 0
days_count = 0
if stay_days > 7:
    days_count = 1
if city_name == "Bansko" or city_name == "Borovets":
    if pack_type == "withEquipment" and vip_card == "yes":
        price = 100 * 0.90
    elif pack_type == "withEquipment" and vip_card == "no":
        price = 100
    elif pack_type == "noEquipment" and vip_card == "yes":
        price = 80 * 0.95
    elif pack_type == "noEquipment" and vip_card == "no":
        price = 80
elif city_name == "Varna" or city_name == "Burgas":
    if pack_type == "withBreakfast" and vip_card == "yes":
        price = 130 * 0.88
    elif pack_type == "withBreakfast" and vip_card == "no":
        price = 130
    elif pack_type == "noBreakfast" and vip_card == "yes":
        price = 100 * 0.93
    elif pack_type == "noBreakfast" and vip_card == "no":
        price = 100
total_price = price * (stay_days - days_count)
if stay_days < 1:
    print("Days must be positive number!")
elif city_name != "Bansko" and city_name != "Borovets" and city_name != "Varna" and city_name != "Burgas":
    print("Invalid input!")
elif pack_type != "withEquipment" and pack_type != "noEquipment" and pack_type != "withBreakfast" \
        and pack_type != "noBreakfast":
    print("Invalid input!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")


