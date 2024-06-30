# В этой программе:

# Вложенная функция ellipse_area(a, b) вычисляет площадь эллипса по его полуосям a и b согласно формуле S = π * a * b.
# С помощью списочного выражения и функции max() находим максимальную площадь среди всех орбит в списке list_of_orbits.
# Далее, используя генератор списка и функцию next(), находим первую орбиту, чья площадь соответствует максимальной площади.
# Результат функции find_farthest_orbit() — кортеж с длинами полуосей эллипса самой далекой планеты.


import math

def find_farthest_orbit(list_of_orbits):
    # Функция для вычисления площади эллипса по его полуосям
    def ellipse_area(a, b):
        return math.pi * a * b
    
    # Найти максимальную площадь среди всех орбит
    max_area = max(ellipse_area(a, b) for a, b in list_of_orbits)
    
    # Найти орбиту с этой максимальной площадью
    farthest_orbit = next((a, b) for a, b in list_of_orbits if ellipse_area(a, b) == max_area)
    
    return farthest_orbit

# Пример использования функции
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
