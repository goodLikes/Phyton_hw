# Задача №1. Решение в группах
# За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output: 2
n = int(input("Введите число 1:"))
m = int (input("Введите число 2:"))

print((n + m - 1) // n)	 #Если не отнять единицу то числа кратные друг другу не будут выдавать верный результат 