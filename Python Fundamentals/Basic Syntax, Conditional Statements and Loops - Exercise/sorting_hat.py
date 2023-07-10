
while True:
    student_name = input()
    if student_name == "Welcome!":
        print(f"Welcome to Hogwarts.")
        break
    elif student_name == "Voldemort":
        print(f"You must not speak of that name!")
        break

    ch_in_name = len(student_name)

    if ch_in_name < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif ch_in_name == 5:
        print(f"{student_name} goes to Slytherin.")
    elif ch_in_name == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif ch_in_name > 6:
        print(f"{student_name} goes to Hufflepuff.")
