pen_packs = int(input())
marker_packs = int(input())
detragent_liters = int(input())
discount_percent = int(input())

pen_price = pen_packs * 5.80
marker_price = marker_packs * 7.20
detragent_price = detragent_liters * 1.20
all_coast = pen_price + marker_price + detragent_price
discount_sum = discount_percent / 100
total_coast = all_coast - (all_coast * discount_sum)

print(total_coast)
