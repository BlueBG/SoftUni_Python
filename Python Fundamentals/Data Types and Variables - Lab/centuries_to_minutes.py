import math

num_of_centuries = int(input())

years = num_of_centuries * 100
days = math.floor(years * 365.2422)
hours = math.floor(days * 24)
minutes = math.floor(hours * 60)

print(f"{num_of_centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
