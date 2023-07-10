import sys

movie_count = int(input())

max_reiting = -sys.maxsize
min_reiting = sys.maxsize
high_reiting_movi = ""
min_reiting_movi = ""
total_reiting = 0

for num in range(1, movie_count + 1):
    movie_name = input()
    reiting = float(input())
    total_reiting += reiting
    if max_reiting < reiting:
        max_reiting = reiting
        high_reiting_movi = movie_name
    elif min_reiting > reiting:
        min_reiting = reiting
        min_reiting_movi = movie_name
averege_reiting = total_reiting / movie_count
print(f"{high_reiting_movi} is with highest rating: {max_reiting:.1f}")
print(f"{min_reiting_movi} is with lowest rating: {min_reiting:.1f}")
print(f"Average rating: {averege_reiting:.1f}")
