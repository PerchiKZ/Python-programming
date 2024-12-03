import json
import os

def load_json(file_path):
    if not os.path.exists(file_path):
        print(f"Файл не знайдено. Створюємо новий файл: {file_path}")
        save_json(file_path, {})
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Помилка декодування JSON. Створюємо порожній файл.")
        return {}

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Дані збережено у файл: {file_path}")

def display_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4))

def add_record(data):
    day = input("Введіть день місяця: ")
    temp = float(input("Введіть температуру: "))
    precipitation = float(input("Введіть кількість опадів: "))
    data[day] = {"temperature": temp, "precipitation": precipitation}
    print("Запис додано.")

def delete_record(data):
    day = input("Введіть день для видалення запису: ")
    if day in data:
        del data[day]
        print("Запис видалено.")
    else:
        print("Запис не знайдено.")

def search_record(data):
    day = input("Введіть день для пошуку: ")
    if day in data:
        print(f"День {day}: {data[day]}")
    else:
        print("Запис не знайдено.")

def analyze_precipitation(data, output_file):
    rain = sum(v['precipitation'] for v in data.values() if v['temperature'] > 0)
    snow = sum(v['precipitation'] for v in data.values() if v['temperature'] <= 0)
    
    result = {"Дощ": rain, "Сніг": snow}
    save_json(output_file, result)
    print(f"Опади у вигляді дощу: {rain} мм, у вигляді снігу: {snow} мм.")

def main():
    input_file = r"C:\Programing Pyton\Lab12\Ex1\precipitation_data.json"
    output_file = r"C:\Programing Pyton\Lab12\Ex1\precipitation_analysis.json"

    data = load_json(input_file)

    while True:
        print("\nОберіть дію:")
        print("1. Виведення JSON-файлу")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Пошук запису")
        print("5. Аналіз опадів")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            display_json(data)
        elif choice == '2':
            add_record(data)
            save_json(input_file, data)
        elif choice == '3':
            delete_record(data)
            save_json(input_file, data)
        elif choice == '4':
            search_record(data)
        elif choice == '5':
            analyze_precipitation(data, output_file)
        elif choice == '6':
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
