# Домашка 3 
""" В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример:
k = 'ноутбук'
# 12 """

def scrabble_score(words):
    # Создаем словари для английских и русских букв
    eng_scores = {
        1: "A.E.I.O.U.L.N.S.T.R",
        2: "D.G",
        3: "B.C.M.P",
        4: "F.H.V.W.Y",
        5: "K",
        8: "J.X",
        10: "Q.Z"
    }

    rus_scores = {
        1: "А.В.Е.И.Н.О.Р.С.Т",
        2: "Д.К.Л.М.П.У",
        3: "Б.Г.Ё.Ь.Я",
        4: "Й.Ы",
        5: "Ж.З.Х.Ц.Ч",
        8: "Ш.Э.Ю",
        10: "Ф.Щ.Ъ"
    }

    # Определяем, на каком языке слова
    is_russian = any('А' <= c <= 'я' for c in words)
    
    # Выбираем соответствующий словарь
    scores = rus_scores if is_russian else eng_scores

    # Создаем словарь с очками для каждой буквы
    letter_scores = {letter: score for score, letters in scores.items() for letter in letters}

    # Вычисляем общую стоимость слова
    total_score = 0
    for word in words.split():
        total_score += sum(letter_scores[letter] for letter in word.upper())
    
    return total_score

# Пример использования
k = 'fuck you'
e = 'Бастард'
print(scrabble_score(k))
print(scrabble_score(e))