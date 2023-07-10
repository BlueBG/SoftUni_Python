favorit_book = input()


checked_books = 0
flag = False
while True:
    checked_books += 1
    cur_book = input()
    if cur_book == favorit_book:

        flag = True
        break

    elif cur_book == "No More Books":
        checked_books -= 1
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
if flag:
    checked_books -= 1
    print(f"You checked {checked_books} books and found it.")

