movi_projection = input()
rows = int(input())
colums = int(input())

all_ticket_price = 0

if movi_projection == "Premiere":
    all_ticket_price = (rows * colums) * 12
elif movi_projection == "Normal":
    all_ticket_price = (rows * colums) * 7.50
else:
    all_ticket_price = (rows * colums) * 5

print(f"{all_ticket_price:.2f} leva")