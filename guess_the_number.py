from random import *

print("Игра: Угадай число")
print("Компьютер загадал число от 1 до 100. Попробуй его отгадать!")

# Компьютер загадывает случайное число
zagadannoe_chislo = randint(1, 100)

# Счетчик попыток игрока
popitki = 0

# Запускаем игровой цикл, пока пользователь не угадает
while True:
    ugadivanie = int(input("Введите ваше число: "))
    popitki = popitki + 1 # Считаем текущую попытку
    
    # Сравниваем число пользователя с загаданным
    if ugadivanie < zagadannoe_chislo:
        print("Загаданное число БОЛЬШЕ.")
    elif ugadivanie > zagadannoe_chislo:
        print("Загаданное число МЕНЬШЕ.")
    else:
        print("Поздравляем! Вы угадали число!")
        print("Количество затраченных попыток:")
        print(popitki)
        break # Выходим из цикла, игра завершена

