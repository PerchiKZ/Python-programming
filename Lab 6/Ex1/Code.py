def extend_list():
    lst = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
    left_elements = list(map(int, input(f"Введіть елементи для доповнення зліва: ").split()))
    right_elements = list(map(int, input(f"Введіть елементи для доповнення справа: ").split()))
    extended_list = left_elements + lst + right_elements
    print("Розширений список:", extended_list)

extend_list()
