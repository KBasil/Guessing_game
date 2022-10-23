from random import *

new_game = 'да'
print('Добро пожаловать в числовую угадайку!')


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= border:
        return True
    return False


while new_game == 'да' or new_game == 'Да' or new_game == 'д' or new_game == 'Д':
    print('Введите число, до которого мы можем загадывать.')
    border = int(input())
    flag = True
    y = randint(1, border)
    counter = 0
    while flag:
        print('Введите число, которое мы загадали:')
        n = input()
        if is_valid(n):
            n = int(n)
            counter += 1
            if y < n:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif y > n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!!!')
                print(f'Кол-во потраченных попыток: {counter}')
                flag = False
        else:
            print(f'А может быть все-таки введем целое число от 1 до {border}?')
    print('Если хотите сыграть еще раз напишите "да"')
    new_game = input()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')