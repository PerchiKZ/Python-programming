import math

def calculate_expression(m):
    if m == 3:
        return "Ділення на нуль неможливе"
    value = (m + 3) / (m - 3)
    if value < 0:
        return "Результат під коренем від’ємний, неможливо обчислити"
    return math.sqrt(value)

def calculate_product(n):
    result = 1
    for i in range(1, n + 1):
        result *= 2 * i
    return result

def main():
    try:
        m = float(input("Введіть число m: "))
        print("Результат обчислення √(m+3/m-3):", calculate_expression(m))
    except ValueError:
        print("Помилка: Введіть правильне число.")

    try:
        n = int(input("Введіть натуральне число n: "))
        if n < 1:
            print("Число n повинно бути натуральним")
        else:
            print("Результат обчислення 2*4*6...(2*n):", calculate_product(n))
    except ValueError:
        print("Помилка: Введіть ціле натуральне число.")

if __name__ == "__main__":
    main()
