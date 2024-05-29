factorial = int(input("Введите N factorial :"))
f = 1
x = 1

while  x <= factorial:
	f = f * x
	x = x + 1
else:
  print(f'Сумма факториала равна : {f}')
