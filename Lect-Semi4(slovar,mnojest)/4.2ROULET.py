import random

def roulette():
    number = random.randint(1, 36)
    return number

def get_color(number):
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    if number in red_numbers:
        return "красное"
    else:
        return "черное"

print("Добро пожаловать в рулетку!")
print("Нажмите Enter, чтобы запустить колесо, или 'q' для выхода.")

while True:
    user_input = input()
    if user_input.lower() == 'q':
        break

    result = roulette()
    color = get_color(result)
    print(f"Выпавшее число: {result} : {color}")
    print("Нажмите Enter, чтобы запустить колесо снова, или 'q' для выхода.")

print("Спасибо за игру!")



