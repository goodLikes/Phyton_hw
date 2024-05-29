# Задача 1: Найдите сумму цифр трехзначного числа. 
# Пример :
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input("Введите число "))
summa = 0 # Переменная summa инициализируется значением 0. В ней будет накапливаться сумма цифр числа.
while a > 0:
    x = a % 10 # Оператор % (остаток от деления) используется для получения последней цифры числа a. Например, если a равно 123, то x будет 3.
    a = a // 10 # Оператор // (целочисленное деление) используется для удаления последней цифры числа a. Например, если a было 123, то после этой операции a станет 12.
    summa = summa + x # Полученная цифра x добавляется к переменной summa.
print("Окончательная сумма:", summa)