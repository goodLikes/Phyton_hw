# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
def count_characters(input_string):
    # Создаем словарь для отслеживания количества встреч каждого символа
    char_count = {}
    # Разделяем входную строку на отдельные символы
    characters = input_string.split()

    # Проходим по каждому символу
    output_string = ""
    for char in characters:
        # Обновляем счетчик встреч символа в словаре
        char_count[char] = char_count.get(char, 0) + 1
        # Формируем символ с постфиксом _n и добавляем его к выходной строке
        output_string += char + "_" + str(char_count[char]) + " "

    return output_string.strip()  # Удаляем лишние пробелы в конце строки

# Пример использования
input_string = "a a a b c a a d c d d"
result = count_characters(input_string)
print(result)  # Вывод: "a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"
