def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print("Введіть рядки для запису у файл (порожній рядок для завершення):")
            while True:
                line = input()
                if not line:  # При введенні порожнього рядка завершуємо запис
                    break
                file.write(line + '\n')
        print(f"Файл {filename} створено.")
    except Exception as e:
        print(f"Помилка створення файлу: {e}")

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            content = infile.read()
            # Видаляємо всі цифри
            content = ''.join(filter(lambda x: not x.isdigit(), content))
            # Забезпечуємо, щоб рядки мали рівно 10 символів
            padded_content = content.replace("\n", " ")  # Прибираємо переноси рядків, замінюючи на пробіл
            for i in range(0, len(padded_content), 10):
                outfile.write(padded_content[i:i+10].rstrip() + '\n')  # Записуємо рядки по 10 символів
        print(f"Файл {output_filename} створено після обробки.")
    except FileNotFoundError:
        print(f"Файл {input_filename} не знайдено.")
    except Exception as e:
        print(f"Помилка обробки файлу: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"\nВміст файлу {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка читання файлу: {e}")

def main():
    input_filename = "TF10_1.txt"
    output_filename = "TF10_2.txt"
    
    print("1. Створити файл TF10_1")
    print("2. Обробити файл TF10_1 та створити TF10_2")
    print("3. Прочитати файл TF10_2")
    print("4. Вийти")
    
    while True:
        try:
            choice = int(input("\nВиберіть опцію (1-4): "))
            if choice == 1:
                create_file(input_filename)
            elif choice == 2:
                process_file(input_filename, output_filename)
            elif choice == 3:
                read_file(output_filename)
            elif choice == 4:
                print("Програма завершена.")
                break
            else:
                print("Невірний вибір. Введіть число від 1 до 4.")
        except ValueError:
            print("Будь ласка, введіть число.")

main()
