movie_name = input()
room_type = input()
ticked_sold = int(input())

total_profit = 0
ticket_price = 0
if movie_name == "A Star Is Born":
    if room_type == "normal":
        ticket_price = 7.50
    elif room_type == "luxury":
        ticket_price = 10.50
    elif room_type == "ultra luxury":
        ticket_price = 13.50
elif movie_name == "Bohemian Rhapsody":
    if room_type == "normal":
        ticket_price = 7.35
    elif room_type == "luxury":
        ticket_price = 9.45
    elif room_type == "ultra luxury":
        ticket_price = 12.75
elif movie_name == "Green Book":
    if room_type == "normal":
        ticket_price = 8.15
    elif room_type == "luxury":
        ticket_price = 10.25
    elif room_type == "ultra luxury":
        ticket_price = 13.25
elif movie_name == "The Favourite":
    if room_type == "normal":
        ticket_price = 8.75
    elif room_type == "luxury":
        ticket_price = 11.55
    elif room_type == "ultra luxury":
        ticket_price = 13.95

total_profit = ticket_price * ticked_sold
print(f"{movie_name} -> {total_profit:.2f} lv.")
