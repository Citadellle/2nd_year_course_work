import matplotlib.pyplot as plt
from inflation import get_actual_inflation_15_25, \
                      get_expect_inflation_pop, \
                      get_expect_inflation_ent

# Получаем словарь с фактической инфляцией
actual_data = get_actual_inflation_15_25()
# Получаем словарь с инфляционными ожиданиями населения
expected_data_population = get_expect_inflation_pop()
# Получаем словарь с инфляционными ожиданиями предприятий
expected_data_enterprises = get_expect_inflation_ent()

# Подготовка данных для оси X (даты) и осей Y (значения)
dates_str = list(expected_data_population.keys())
dates = [date for date in dates_str]

# Получаем значения
actual = [actual_data[date] for date in dates_str]
expectations_pop = [expected_data_population.get(date, None) for date in dates_str]
expected_ent = [expected_data_enterprises.get(date, None) for date in dates_str]

# Создаем график
plt.figure(figsize=(12, 7))

# Строим линии графиков
plt.plot(dates, actual, marker='o', linewidth=2, markersize=6, 
         label='Фактическая инфляция', color='blue')
plt.plot(dates, expectations_pop, marker='s', linewidth=2, markersize=6, 
         label='Инфляционные ожидания населения', color='red')
plt.plot(dates, expected_ent, marker='s', linewidth=2, markersize=6, 
         label='Инфляционные ожидания предприятий', color='orange')

# Настраиваем внешний вид графика
plt.title('Сравнение фактической инфляции, инфляционных ожиданий населения и предприятий', 
          fontsize=16, fontweight='bold')
plt.xlabel('Период (месяц.год)', fontsize=12)
plt.ylabel('Инфляция (%)', fontsize=12)
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3, linestyle='--')

# Добавляем значения на график
for i, (month, actual_val, exp_pop_val, exp_ent_val) in enumerate(zip(dates, actual, expectations_pop, expected_ent)):
    plt.annotate(f'{actual_val:.1f}', xy=(i, actual_val), xytext=(0, 5), 
                textcoords='offset points', fontsize=7, ha='center', color='blue')
    if exp_pop_val is not None:
        plt.annotate(f'{exp_pop_val:.1f}', xy=(i, exp_pop_val), xytext=(0, -15), 
                    textcoords='offset points', fontsize=7, ha='center', color='red')
    if exp_ent_val is not None:
        plt.annotate(f'{exp_ent_val:.1f}', xy=(i, exp_ent_val), xytext=(0, 10), 
                    textcoords='offset points', fontsize=7, ha='center', color='orange')

# Поворачиваем подписи оси X для лучшей читаемости
plt.xticks(rotation=45, ha='right', fontsize=8)

# Сохранем изображение графика
plt.savefig('Все.png', dpi=1000, bbox_inches='tight')

plt.tight_layout()
plt.show()