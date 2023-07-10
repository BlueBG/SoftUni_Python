import math

video_card_price = int(input())
conector_price = int(input())
electricity_per_day = float(input())
one_card_profit_day = float(input())


total_video = video_card_price * 13
total_conectors = conector_price * 13
total_component_price = total_video + total_conectors + 1000
profit_per_day = one_card_profit_day - electricity_per_day
total_profit = profit_per_day * 13
payback_days = math.ceil(total_component_price / total_profit)

print(total_component_price)
print(payback_days)
