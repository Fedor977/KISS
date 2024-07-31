"""
Принцип KISS в Python:

1. Простота: избегайте излишней сложности.
2. Легкость понимания: код должен быть понятен без дополнительных комментариев.
"""

# Пример: Класс для вычисления средней температуры

# Сложный способ (не KISS)
class TemperatureAnalyzerComplex:
    def __init__(self, temperatures):
        self.temperatures = temperatures  # Инициализация списка температур

    def calculate_average(self):
        if not self.temperatures:  # Проверка, если список пуст
            return 0
        total = 0
        for temp in self.temperatures:  # Проход по всем температурам
            total += temp
        return total / len(self.temperatures)  # Возврат средней температуры

# Простой способ (KISS)
class TemperatureAnalyzer:
    def __init__(self, temperatures):
        self.temperatures = temperatures  # Инициализация списка температур

    def calculate_average(self):
        return sum(self.temperatures) / len(self.temperatures) if self.temperatures else 0
        # Использование встроенных функций sum и len для вычисления средней температуры

# Демонстрация работы KISS
temperatures = [22, 24, 26, 23, 25]
analyzer = TemperatureAnalyzer(temperatures)
average = analyzer.calculate_average()
print(f"Средняя температура: {average}")  # Вывод средней температуры
