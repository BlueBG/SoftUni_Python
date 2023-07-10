first_number = int(input())
second_number = int(input())
number_operator = input()

result = 0
even_or_odd = ""
if number_operator == "+":
    result = first_number + second_number
elif number_operator == "-":
    result = first_number - second_number
elif number_operator == "*":
    result = first_number * second_number
elif second_number == 0 and number_operator == "%":
    print(f"Cannot divide {first_number} by zero")
elif number_operator == "%":
    result = first_number % second_number
    print(f"{first_number} % {second_number} = {result}")
elif second_number == 0 and number_operator == "/":
    print(f"Cannot divide {first_number} by zero")
elif number_operator == "/":
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {result:.2f}")
if (number_operator == "+" or number_operator == "-" or number_operator == "*") and result % 2 == 0:
    even_or_odd = "even"
    print(f"{first_number} {number_operator} {second_number} = {result} - {even_or_odd}")
elif (number_operator == "+" or number_operator == "-" or number_operator == "*") and result % 2 != 0:
        even_or_odd = "odd"
        print(f"{first_number} {number_operator} {second_number} = {result} - {even_or_odd}")
