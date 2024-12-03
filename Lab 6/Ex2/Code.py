def remove_duplicates():
    lst = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print("Список без повторів:", unique_list)

remove_duplicates()
