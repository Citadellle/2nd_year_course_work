import matplotlib.pyplot as plt
from inflation import get_actual_inflation_15_25, get_expect_inflation_ent

# Получаем словарь с фактической инфляцией
actual_inflation = get_actual_inflation_15_25()

# Получаем словарь с инфляционными ожиданиями предприятий
expectations = get_expect_inflation_ent()

# Фильтруем фактическую инфляцию только для тех месяцев, которые есть в ожиданиях
filtered_actual = {month: actual_inflation[month] for month in expectations.keys() if month in actual_inflation}

# Сортируем данные по датам
sorted_months = sorted(filtered_actual.keys(), key=lambda x: (int(x.split('.')[1]), int(x.split('.')[0])))
sorted_actual = [filtered_actual[month] for month in sorted_months]
sorted_expectations = [expectations[month] for month in sorted_months]
 
# Создаем график
plt.figure(figsize=(12, 7))

# Строим линии графиков
plt.plot(sorted_months, sorted_actual, marker='o', linewidth=2, markersize=6, 
         label='Фактическая инфляция', color='blue')
plt.plot(sorted_months, sorted_expectations, marker='s', linewidth=2, markersize=6, 
         label='Инфляционные ожидания предприятий', color='red')

# Настраиваем внешний вид графика
plt.title('Сравнение фактической инфляции и инфляционных ожиданий предприятий', 
          fontsize=16, fontweight='bold')
plt.xlabel('Период (месяц.год)', fontsize=12)
plt.ylabel('Инфляция (%)', fontsize=12)
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3, linestyle='--')

# Поворачиваем подписи оси X для лучшей читаемости
plt.xticks(rotation=45, ha='right', fontsize=8)

# Добавляем значения на график (опционально)
for i, (month, actual, exp) in enumerate(zip(sorted_months, sorted_actual, sorted_expectations)):
    plt.annotate(f'{actual:.1f}', xy=(i, actual), xytext=(0, 10), 
                textcoords='offset points', fontsize=7, ha='center', color='blue')
    plt.annotate(f'{exp:.1f}', xy=(i, exp), xytext=(0, -15), 
                textcoords='offset points', fontsize=7, ha='center', color='red')

# Сохранем изображение графика
plt.savefig('Ожидания предприятий.png', dpi=1000, bbox_inches='tight')

plt.tight_layout()
plt.show()