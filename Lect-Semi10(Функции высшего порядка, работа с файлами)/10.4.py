# В этом примере:

# Лямбда-выражение lambda x: x просто возвращает аргумент x без изменений.
# Функция map применяет это лямбда-выражение ко всем элементам списка values, создавая список transformed_values, который является копией исходного списка values.
# После этого проводится проверка с помощью условного оператора if, чтобы убедиться, что transformed_values действительно равен values. Если условие выполняется, выводится 'ok', иначе 'fail'.
# Таким образом, программа успешно демонстрирует, что transformed_values является копией values, что подтверждается выводом 'ok'.

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda x: x
transformed_values = list(map(transformation, values))

# Проверка, что transformed_values является копией values
if values == transformed_values:
    print('ok')
else:
    print('fail')
