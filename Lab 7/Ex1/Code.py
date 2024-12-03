def print_all(dictionary):
    print("\nВсі записи у словнику:")
    for key, value in dictionary.items():
        print(f"День {key}: Опади {value['rainfall']} мм, Температура {value['temperature']}°C")

def add_record(dictionary):
    try:
        day = int(input("Введіть день (1-31): "))
        if day in dictionary:
            print(f"Запис для дня {day} вже існує.")
            return
        rainfall = float(input("Введіть кількість опадів (мм): "))
        temperature = float(input("Введіть температуру (°C): "))
        dictionary[day] = {"rainfall": rainfall, "temperature": temperature}
        print(f"Запис для дня {day} додано.")
    except ValueError:
        print("Невірний формат введення даних.")

def remove_record(dictionary):
    try:
        day = int(input("Введіть день для видалення (1-31): "))
        if day not in dictionary:
            print(f"Запис для дня {day} не знайдено.")
            return
        del dictionary[day]
        print(f"Запис для дня {day} видалено.")
    except ValueError:
        print("Невірний формат введення даних.")

def view_sorted(dictionary):
    print("\nСловник за відсортованими днями:")
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        print(f"День {key}: Опади {value['rainfall']} мм, Температура {value['temperature']}°C")

def calculate_snow_rain(dictionary):
    snow = sum(value["rainfall"] for value in dictionary.values() if value["temperature"] <= 0)
    rain = sum(value["rainfall"] for value in dictionary.values() if value["temperature"] > 0)
    print(f"\nОпади у вигляді снігу: {snow} мм")
    print(f"Опади у вигляді дощу: {rain} мм")

def main():
    precipitation_data = {
        1: {"rainfall": 5, "temperature": -2},
        2: {"rainfall": 3, "temperature": 1},
        3: {"rainfall": 8, "temperature": -1},
        4: {"rainfall": 10, "temperature": 3},
        5: {"rainfall": 7, "temperature": -5},
    }

    while True:
        print("\nМеню:")
        print("1. Вивести всі записи")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Переглянути словник за відсортованими днями")
        print("5. Обчислити опади у вигляді снігу та дощу")
        print("6. Вийти")
        choice = input("Виберіть опцію (1-6): ")

        if choice == "1":
            print_all(precipitation_data)
        elif choice == "2":
            add_record(precipitation_data)
        elif choice == "3":
            remove_record(precipitation_data)
        elif choice == "4":
            view_sorted(precipitation_data)
        elif choice == "5":
            calculate_snow_rain(precipitation_data)
        elif choice == "6":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()
