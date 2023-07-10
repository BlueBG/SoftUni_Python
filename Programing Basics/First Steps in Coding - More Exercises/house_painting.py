x_house = float(input())
y_house = float(input())
h_house = float(input())

side_wall = x_house * y_house
window_size = 1.50 * 1.50
total_side_wall_size = (2 * side_wall) - (2 * window_size)
back_side_wall = x_house * x_house
door_size = 1.2 * 2
front_back_wall_size = (back_side_wall * 2) - door_size
total_house_size = total_side_wall_size + front_back_wall_size
green_paint_needed = total_house_size / 3.4

roof_rectangles = (x_house * y_house) * 2
roof_triangles = 2 * (x_house * h_house / 2)
total_roof_size = roof_triangles + roof_rectangles
red_paint_needed = total_roof_size / 4.3

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
