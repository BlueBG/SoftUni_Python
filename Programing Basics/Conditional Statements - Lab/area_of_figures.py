from math import pi
figure = input()

area = 0

if figure == "square":
    side_a = float(input())
    area = side_a * side_a
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
    print(f"{area:.3f}")
elif figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = 1 / 2 * side_a * side_b
    print(f"{area:.3f}")
