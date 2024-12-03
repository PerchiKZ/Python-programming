n = int(input("Введіть кількість елементів масиву: "))
array = [int(input(f"Елемент {i + 1}: ")) for i in range(n)]
positive_elements = [x for x in array if x > 0]
print("Додатні елементи:", *positive_elements)
