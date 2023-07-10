while True:
    enter_word = input()

    if enter_word == "End":
        break

    if enter_word == "SoftUni":
        continue

    converted_ch = ""

    for ch in enter_word:
        converted_ch += ch * 2
    print(converted_ch)
