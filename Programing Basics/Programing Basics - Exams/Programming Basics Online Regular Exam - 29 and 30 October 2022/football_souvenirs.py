team_name = input()
suvenir_type = input()
suvenir_count = int(input())

flag_price = 0
caps_price = 0
posters_price = 0
stickers_price = 0
total_price = 0
valid_team = False
valid_stock = False

if team_name != "Argentina" and team_name != "Brazil" and team_name != "Croatia" and team_name != "Denmark":
    valid_team = True
elif suvenir_type != "flags" and suvenir_type != "caps" and suvenir_type != "posters" and suvenir_type != "stickers":
    valid_stock = True

if suvenir_type == "flags":
    if team_name == "Argentina":
        flag_price = 3.25
        total_price = flag_price * suvenir_count
    elif team_name == "Brazil":
        flag_price = 4.20
        total_price = flag_price * suvenir_count
    elif team_name == "Croatia":
        flag_price = 2.75
        total_price = flag_price * suvenir_count
    elif team_name == "Denmark":
        flag_price = 3.10
        total_price = flag_price * suvenir_count

elif suvenir_type == "caps":
    if team_name == "Argentina":
        caps_price = 7.20
        total_price = caps_price * suvenir_count
    elif team_name == "Brazil":
        caps_price = 8.50
        total_price = caps_price * suvenir_count
    elif team_name == "Croatia":
        caps_price = 6.90
        total_price = caps_price * suvenir_count
    elif team_name == "Denmark":
        caps_price = 6.50
        total_price = caps_price * suvenir_count

elif suvenir_type == "posters":
    if team_name == "Argentina":
        posters_price = 5.10
        total_price = posters_price * suvenir_count
    elif team_name == "Brazil":
        posters_price = 5.35
        total_price = posters_price * suvenir_count
    elif team_name == "Croatia":
        posters_price = 4.95
        total_price = posters_price * suvenir_count
    elif team_name == "Denmark":
        posters_price = 4.80
        total_price = posters_price * suvenir_count

elif suvenir_type == "stickers":
    if team_name == "Argentina":
        stickers_price = 1.25
        total_price = stickers_price * suvenir_count
    elif team_name == "Brazil":
        stickers_price = 1.20
        total_price = stickers_price * suvenir_count
    elif team_name == "Croatia":
        stickers_price = 1.10
        total_price = stickers_price * suvenir_count
    elif team_name == "Denmark":
        stickers_price = 0.90
        total_price = stickers_price * suvenir_count


if valid_stock:
    print("Invalid stock!")
elif valid_team:
    print("Invalid country!")
else:
    print(f"Pepi bought {suvenir_count} {suvenir_type} of {team_name} for {total_price:.2f} lv.")
