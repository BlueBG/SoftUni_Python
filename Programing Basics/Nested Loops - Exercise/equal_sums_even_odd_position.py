start_num = int(input())
end_num = int(input())

for number in range(start_num, end_num + 1):
    hundred_thousand = number // 100000
    ten_thousand = (number // 10000) % 10
    thousand = (number // 1000) % 10
    hundred = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10
    sum_even = ten_thousand + hundred + units
    sum_odd = hundred_thousand + thousand + tens

    if sum_even == sum_odd:
        print(number, end=" ")

