def calculate_x(a, b):
    if a > b:
        return a * b + 21
    elif a == b:
        return -5
    else: 
        return 3 * a / b + 1

def main():
    try:
        a = float(input("Введіть число a (додатнє): "))
        b = float(input("Введіть число b (додатнє): "))

        if a <= 0 or b <= 0:
            print("Помилка: числа a та b повинні бути додатніми")
            return

        x = calculate_x(a, b)
        print(f"Результат X: {x}")

    except ValueError:
        print("Помилка: введіть коректні числові значення")

if __name__ == "__main__":
    main()