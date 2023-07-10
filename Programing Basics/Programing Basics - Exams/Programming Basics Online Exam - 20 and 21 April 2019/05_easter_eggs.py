import sys

eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs_count = -sys.maxsize
max_eggs_color = ""

for num in range(1, eggs_count + 1):
    color = input()
    if color == "red":
        red_eggs += 1
    elif color == "orange":
        orange_eggs += 1
    elif color == "blue":
        blue_eggs += 1
    elif color == "green":
        green_eggs += 1
    if red_eggs > max_eggs_count:
        max_eggs_count = red_eggs
    elif orange_eggs > max_eggs_count:
        max_eggs_count = orange_eggs
    elif blue_eggs > max_eggs_count:
        max_eggs_count = blue_eggs
    elif green_eggs > max_eggs_count:
        max_eggs_count = green_eggs
if max_eggs_count == red_eggs:
    max_eggs_color = "red"
elif max_eggs_count == orange_eggs:
    max_eggs_color = "orange"
elif max_eggs_count == blue_eggs:
    max_eggs_color = "blue"
elif max_eggs_count == green_eggs:
    max_eggs_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs_count} -> {max_eggs_color}")
