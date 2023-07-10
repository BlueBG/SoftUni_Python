fruit_type = input()

if fruit_type == "banana" or fruit_type == "apple" or fruit_type == "kiwi" or fruit_type == "cherry" \
        or fruit_type == "lemon" or fruit_type == "grapes":
    print("fruit")
elif fruit_type == "tomato" or fruit_type == "cucumber" or fruit_type == "pepper" or fruit_type == "carrot":
    print("vegetable")
else:
    print("unknown")
