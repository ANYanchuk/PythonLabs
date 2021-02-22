from functions import load_json, save_json

import msvcrt

case = {'1': lambda: load_json(input('Введите название файла для чтения: ')),
        '2': lambda: save_json(input('Введите название файла для записи: ')),   
        '3': lambda: exit(),
        }

def menu():
    print('1. Прочитать данные из файла: ')
    print('2. Записать данные в файл: ')
    print('3. Выйти')
    sign = msvcrt.getch().decode('ASCII')
    case[sign]()
    menu()
