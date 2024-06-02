#ЗАДАЧА N_2
""" Дана последовательность из N целых чисел и число 
K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – 
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3] """

list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
 n = int(input("#""Введите число:")) # пользователь вводит целое число
 list_1.append(n) 
print(list_1) 
k = int(input())
k = k % len(list_1)

list_res1 = []

for i in range(k):
	list_res1.append(list_1[len(list_1) - 1 -i])
print(list_res1)

for i in range(len(list_1) - k):
	list_res1.append(list_1[i])
print(list_res1)



