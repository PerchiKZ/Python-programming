word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

unique_letters_word1 = {ch for ch in word1 if word1.count(ch) == 1}
unique_letters_word2 = {ch for ch in word2 if word2.count(ch) == 1}

common_unique_letters = unique_letters_word1.intersection(unique_letters_word2)

if common_unique_letters:
    print("Літери, які зустрічаються в обох словах тільки один раз:", "".join(common_unique_letters))
else:
    print("Немає літер, які зустрічаються в обох словах тільки один раз.")