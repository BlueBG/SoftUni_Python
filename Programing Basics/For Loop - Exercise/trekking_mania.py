group_count = int(input())

musala_peek = 0
monblan_peek = 0
kilimadjaro_peek = 0
k2_peek = 0
everest_peek = 0
total_people = 0

for i in range(1, group_count + 1):
    people_count = int(input())
    total_people += people_count
    if people_count <= 5:
        musala_peek += people_count
    elif 5 < people_count <= 12:
        monblan_peek += people_count
    elif 12 < people_count <= 25:
        kilimadjaro_peek += people_count
    elif 25 < people_count <= 40:
        k2_peek += people_count
    else:
        everest_peek += people_count
musala_percent = (musala_peek / total_people) * 100
monblan_percent = (monblan_peek / total_people) * 100
kilimadjaro_percent = (kilimadjaro_peek / total_people) * 100
k2_percent = (k2_peek / total_people) * 100
everest_percent = (everest_peek / total_people) * 100
print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimadjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
