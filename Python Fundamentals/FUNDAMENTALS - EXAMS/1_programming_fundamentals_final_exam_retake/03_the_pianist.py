number_of_pieces = int(input())

artist_info = {}
piece_info = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    artist_info[piece] = composer
    piece_info[piece] = key

while True:
    command_line = input().split("|")
    command = command_line[0]

    if command == "Stop":
        break

    if command == "Add":
        piece = command_line[1]
        composer = command_line[2]
        key = command_line[3]

        if piece in artist_info.keys():
            print(f"{piece} is already in the collection!")
        else:
            artist_info[piece] = composer
            piece_info[piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        piece = command_line[1]

        if piece in artist_info.keys():
            artist_info.pop(piece)
            piece_info.pop(piece)
            print(f"Successfully removed {piece}!""")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        piece = command_line[1]
        new_key = command_line[2]

        if piece in piece_info.keys():
            piece_info[piece] = new_key

            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece in artist_info.keys():
    composer = artist_info[piece]
    key = piece_info[piece]

    print(f"{piece} -> Composer: {composer}, Key: {key}")
