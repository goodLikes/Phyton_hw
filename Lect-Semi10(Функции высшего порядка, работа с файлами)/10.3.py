# Задача 2: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


# Исходный список
numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Заданный диапазон
min_value = 1
max_value = 10

# Поиск индексов элементов, удовлетворяющих условию
indices = [index for index, value in enumerate(numbers) if min_value <= value <= max_value]

# Вывод результатов
print(indices)
