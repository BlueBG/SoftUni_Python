start_num = int(input())
end_num = int(input())

for i in range(start_num, end_num + 1):
    symbol_of_ascii = chr(i)
    print(symbol_of_ascii, end=" ")
