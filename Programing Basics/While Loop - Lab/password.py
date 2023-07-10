username = input()
password = input()
insert_data = input()
while insert_data != password:
    insert_data = input()
else:
    print(f"Welcome {username}!")

