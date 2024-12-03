def main():
    n = int(input("Введіть ціле число N (2 <= N <= 8): "))
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    main()