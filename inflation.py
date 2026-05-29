import pandas as pd
import json
from datetime import datetime

# Фактическая инфляция с 2015 по 2025
def get_actual_inflation_15_25(file_path = 'actual_inflation_2015_2025.xlsx'):
    # Чтение Excel файла
    df = pd.read_excel(file_path, dtype = {0: str})
    
    # Получаем первый и третий столбцы
    dates = df.iloc[:, 0]
    values = df.iloc[:, 2]
    
    # Создаем список кортежей (дата_объект, строка_даты, значение)
    data = []
    for date, value in zip(dates, values):
        # Преобразуем в datetime объект
        date_obj = datetime.strptime(date, '%m.%Y')
        date_str = date

        if date_obj.year < 2026:
            data.append((date_obj, date_str, value))
    
    # Сортируем по дате (по возрастанию)
    data.sort(key=lambda x: x[0])
    
    # Создаем отсортированный словарь
    sorted_dict = {date_str: value for _, date_str, value in data}
    
    return sorted_dict

# Инфляционные ожидания населения
def get_expect_inflation_pop(file_path = 'expected_inflation_population.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

# Инфляционные ожидания предприятий
def get_expect_inflation_ent(file_path = 'expected_inflation_enterprises.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

# Фактическая инфляция с 2014 по 2025
def get_actual_inflation_14_25(file_path='actual_inflation_2014_2025.xlsx'):
    # Чтение Excel файла
    df = pd.read_excel(file_path, dtype={0: str})
    
    # Получаем первый и третий столбцы
    dates = df.iloc[:, 0]
    values = df.iloc[:, 2]
    
    # Создаем список кортежей (дата_объект, строка_даты, значение)
    data = []
    for date, value in zip(dates, values):
        # Преобразуем в datetime объект
        date_obj = datetime.strptime(date, '%m.%Y')
        date_str = date

        if date_obj.year < 2026:
            data.append((date_obj, date_str, value))
    
    # Сортируем по дате (по возрастанию)
    data.sort(key=lambda x: x[0])
    
    # Создаем отсортированный словарь
    sorted_dict = {date_str: value for _, date_str, value in data}
    
    return sorted_dict

# Адаптивная инфляция
def get_adaptive_expectations(actual_inflation: dict = get_actual_inflation_14_25()) -> dict:
    # Сортируем месяцы в хронологическом порядке
    sorted_months = sorted(actual_inflation.keys(), key=lambda d: datetime.strptime(d, '%m.%Y'))
    
    expectations = {}
    
    # Начинаем с третьего месяца (индекс 2), так как нужны два предыдущих
    for i in range(2, len(sorted_months)):
        current_month = sorted_months[i]
        prev_1 = sorted_months[i-1]
        prev_2 = sorted_months[i-2]
        
        # Считаем среднее значение за два предыдущих месяца
        avg = (actual_inflation[prev_1] + actual_inflation[prev_2]) / 2
        
        # Записываем результат, округляя до 2 знаков после запятой для удобства
        expectations[current_month] = round(avg, 2)
        
    return expectations