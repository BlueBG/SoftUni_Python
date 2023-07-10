import math

vineyard_square_meter = int(input())
grape_per_square_meter = float(input())
wine_needed = int(input())
worker_count = int(input())

grape_amaunt = vineyard_square_meter * grape_per_square_meter
grape_for_wine = grape_amaunt * 0.40
wine_amaunt_lt = grape_for_wine / 2.50
roundned_wine_lt = math.floor(wine_amaunt_lt)
diff = abs(wine_needed - wine_amaunt_lt)
rounded_diff = math.ceil(diff)
wine_for_workers = diff / worker_count
rounded_workers_wine = math.ceil(wine_for_workers)


if wine_amaunt_lt >= wine_needed:
    print(f"Good harvest this year! Total wine: {roundned_wine_lt} liters.")
    print(f"{rounded_diff} liters left -> {rounded_workers_wine} liters per person.")
else:
    rounded_diff = math.floor(diff)
    print(f"It will be a tough winter! More {rounded_diff} liters wine needed.")