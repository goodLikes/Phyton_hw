# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
def count_unique_words(text):
    # Разделить текст на слова
    words = text.split()
    # Преобразовать список слов во множество для удаления дубликатов
    unique_words = set(words)
    # Подсчитать количество уникальных слов
    count = len(unique_words)
    return count

# Пример использования
input_text = input("Введите текст: ")
result = count_unique_words(input_text)
print(result)  # Вывод: количество различных слов в тексте
