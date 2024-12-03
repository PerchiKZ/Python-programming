sentence = input("Введіть речення: ")

words_with_o = [word for word in sentence.split() if 'о' in word or 'О' in word]

if words_with_o:
    print("Слова, які містять хоча б одну літеру 'о':", ", ".join(words_with_o))
else:
    print("Немає слів, які містять літеру 'о'.")
