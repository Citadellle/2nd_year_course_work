import matplotlib.pyplot as plt
from inflation import get_actual_inflation_15_25, get_adaptive_expectations

# Получение данных из функций
actual_data = get_actual_inflation_15_25()
expected_data = get_adaptive_expectations()

# Подготовка данных для оси X (даты) и осей Y (значения)
dates_str = list(actual_data.keys())
dates = [date for date in dates_str]

actual_values = [actual_data[date] for date in dates_str]
expected_values = [expected_data[date] for date in dates_str]

# Настройка холста для графика
plt.figure(figsize=(14, 7))

# Построение графиков
plt.plot(dates, actual_values, label='Фактическая инфляция', color='blue')
plt.plot(dates, expected_values, label='Адаптивные ожидания', color='red', linestyle='--')

# Настраиваем внешний вид графика
plt.title('Динамика фактической инфляции и адаптивных ожиданий', 
          fontsize=16, fontweight='bold')
plt.xlabel('Период (месяц.год)', fontsize=12)
plt.ylabel('Инфляция (%)', fontsize=12)
plt.legend(fontsize=11, loc='upper right')
plt.grid(True, alpha=0.3, linestyle='--')

# Настройка оси OX
plt.xticks(rotation=90, ha="right", fontsize=5)

# Сохранем изображение графика
plt.savefig('Адаптивный метод.png', dpi=1000, bbox_inches='tight')

plt.tight_layout()
plt.show()