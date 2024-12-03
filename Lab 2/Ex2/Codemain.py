import math
from Codemod import calculate_product
def calculate_product(n):
    result = 1
    for i in range(1, n + 1):
        result *= 2 * i
    return result

def main():

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
