from functions import load_json, save_json, save_csv

import msvcrt

case = {'1': lambda: load_json(input('Введите название файла для чтения: ')),
        '2': lambda: save_json(input('Введите название файла для записи: ')),
        '3': lambda: save_csv(input('Введите название файла для записи: ')),
        '4': lambda: exit(),
        }


def menu():
    print('1. Прочитать данные из файла: ')
    print('2. Записать данные в json файл: ')
    print('3. Записать данные в csv файл: ')
    print('4. Выйти')
    sign = msvcrt.getch().decode('ASCII')
    case[sign]()
    menu()
