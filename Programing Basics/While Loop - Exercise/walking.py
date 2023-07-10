input_line = input()

steps_count = 0

while input_line != "Going home":
    steps_walk = int(input_line)
    steps_count += steps_walk
    if steps_count >= 10000:
        break

    input_line = input()

if input_line == "Going home":
    home_steps = int(input())
    steps_count += home_steps

diff = abs(steps_count - 10000)

if steps_count >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
elif steps_count <= 10000:
    print(f"{diff} more steps to reach goal.")
