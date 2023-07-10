devisor_num = int(input())
boundary_num = int(input())

largerst_num = 0

for i in range(1, boundary_num + 1):
    if i % devisor_num == 0:
        largerst_num = i
print(largerst_num)
