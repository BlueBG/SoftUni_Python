total_pages = int(input())
pages_per_houer = int(input())
days_for_book = int(input())

book_read_houers = total_pages // pages_per_houer
needed_day_time = book_read_houers / days_for_book

print(needed_day_time)