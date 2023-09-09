# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

n = randint(1, 100)
print(n)
s = 1
print('Играем в игру угадайка!!!')
print('У Вас будет 10 попыток что бы отгадать число которое загадал компьютер')
k = int(input('Ваше первое число: '))
while s != 10 and k != n:
    print(f'осталось {10 - s}')
    print('Ваше чило БОЛЬШЕ загаданного' if k > n else 'Ваше чило МЕНЬШЕ загаданного')
    k = int(input('Какое число будет следующим: '))
    s += 1

print(f'Вы угадали!!! Это число: {n}' if s != 10 else 'У вас закончились попытки. Вы не отгадали')
