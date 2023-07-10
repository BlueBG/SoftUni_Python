movie_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

total_ticket_price = ticket_price * tickets_count * days_count
rent_purcent = total_ticket_price * percent_for_cinema / 100
total_profit = total_ticket_price - rent_purcent
print(f"The profit from the movie {movie_name} is {total_profit:.2f} lv.")