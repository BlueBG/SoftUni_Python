the_most_powerful_word = 0
the_most_powerful_word_text = ""

while True:
    word = input()

    if word == "End of words":
        break
    current_counter_of_chars = 0
    for i in range(len(word)):
        current_counter_of_chars += ord(word[i])

    if word[0].lower() in 'aeiouy':
        current_counter_of_chars = current_counter_of_chars * len(word)
    else:
        current_counter_of_chars = int(current_counter_of_chars / len(word))

    if current_counter_of_chars > the_most_powerful_word:
        the_most_powerful_word = current_counter_of_chars
        the_most_powerful_word_text = word

print(the_most_powerful_word_text, the_most_powerful_word)