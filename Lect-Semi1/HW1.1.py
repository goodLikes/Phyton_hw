""" Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
ПРИМЕР :
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10 """

""" bird = float(input("Введите кол-во журавлей :"))
summ1 = 0
summ2 = 0
summ3 = 0
summ1 = bird // 2
summ2 = summ1 // 2
summ3 = summ2
print(f'Катя сделала - {summ1}')
print(f'Петя сделал - {summ2}')
print(f'Сережа сделал - {summ3}') """

bird = float(input("Введите кол-во журавлей: "))

# Расчет количества журавликов, сделанных каждым
katya = bird / 2
petya = katya / 2
serezha = petya

print(f'Катя сделала - {katya}')
print(f'Петя сделал - {petya}')
print(f'Сережа сделал - {serezha}')
