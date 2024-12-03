def squares_set():
    n = int(input("Введіть кількість елементів множини від 1 до межах 31: "))
    if n > 31 or n < 1:
        print("Неправильне значення. Введіть число від 1 до 31.")
        return
    squares = [i**2 for i in range(1, 32) if i**2 <= 1000]
    result = squares[:n]
    print("Результуюча множина квадратів:", result)

squares_set()
