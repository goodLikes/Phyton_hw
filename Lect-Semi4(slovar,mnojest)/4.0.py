# Задача №25.
""" Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 """
""" 
str1 = input()  # Получаем ввод от пользователя
res = {}  # Создаем пустой словарь для подсчета символов
for i in str1:  # Проходимся по каждому символу в строке
    print(f'{i}_{res[i]}' if i in res else i, end=' ')  # Если символ уже был, выводим его с индексом, иначе просто символ
    res[i] = res.get(i, 0) + 1  # Обновляем счетчик символов в словаре """
 
str1 = input()
res = {}
for i in str1:
    print(f'{i}_{res[i]}' if i in res else i, end=' ')
    res[i] = res.get(i, 0) + 1

