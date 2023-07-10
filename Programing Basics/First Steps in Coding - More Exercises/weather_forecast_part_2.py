temperature = float(input())

if 5 <= temperature <= 11.9:
    print("Cold")
elif 12 <= temperature <= 14.9:
    print("Cool")
elif 15 <= temperature <= 20:
    print("Mild")
elif 20.1 <= temperature <= 25.9:
    print("Warm")
elif 26 <= temperature <= 35:
    print("Hot")
else:
    print("unknown")