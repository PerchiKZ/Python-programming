import csv

# Шлях до вхідного і вихідного файлів
input_file = r"C:\Programing Pyton\Lab 11\Ex1\worldbank_data.csv"
output_file = r"C:\Programing Pyton\Lab 11\Ex1\exports_analysis_2019.csv"

try:
    # Відкриття CSV-файлу для читання
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Зчитування заголовків
        
        # Індекс колонки за 2019 рік
        year_index = headers.index("2019 [YR2019]")
        
        # Зчитуємо дані у список, виключаючи пусті значення або нечислові дані
        data = [
            row for row in reader 
            if row[year_index].strip().replace('.', '', 1).isdigit() and row[0] == "Exports of goods and services (% of GDP)"
        ]

    # Конвертуємо дані у формат (країна, значення)
    export_values = [
        (row[2], float(row[year_index]))  # row[2] — назва країни
        for row in data
    ]

    # Перевірка наявності оброблених даних
    if not export_values:
        print("Дані для обробки відсутні або некоректні.")
    else:
        # Знаходимо мінімальне та максимальне значення
        max_country, max_value = max(export_values, key=lambda x: x[1])
        min_country, min_value = min(export_values, key=lambda x: x[1])

        # Виведення даних на екран
        print(f"{'Країна':<30} {'Значення (% від ВВП)':<20}")
        for country, value in export_values:
            print(f"{country:<30} {value:<20}")

        # Запис результатів у новий CSV-файл
        with open(output_file, mode='w', encoding='utf-8', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(["Країна з найбільшим показником", "Значення (% від ВВП)"])
            writer.writerow([max_country, max_value])
            writer.writerow(["Країна з найменшим показником", "Значення (% від ВВП)"])
            writer.writerow([min_country, min_value])
            
            print("\nРезультати успішно записані у файл:", output_file)

except FileNotFoundError:
    print("Помилка: Файл не знайдено за вказаним шляхом.")
except Exception as e:
    print("Сталася помилка:", str(e))
