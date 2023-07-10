movie_name = input()

student_count = 0
standard_count = 0
kid_count = 0
total_tickets = 0

while movie_name != "Finish":
    free_seats_per_movie = int(input())
    free_space = free_seats_per_movie
    sold_tickets = 0
    while free_space > 0:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_count += 1
        elif ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "kid":
            kid_count += 1
        total_tickets += 1
        sold_tickets += 1
        free_space -= 1
    print(f"{movie_name} - {sold_tickets / free_seats_per_movie * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_count / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_count / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_count / total_tickets * 100:.2f}% kids tickets.")
