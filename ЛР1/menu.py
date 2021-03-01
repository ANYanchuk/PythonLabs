from functions import JsonManager

manager = JsonManager()


def process_csv():
    print('Обработка CSV не реализована')


cases = {'json': manager.process_file, 'csv': process_csv}


def menu():
    file = input("\033[38mВведите тип файла!\n")
    try:
        cases[file.lower()]()
    except KeyError:
        print(f"\033[31mНедоступный тип тип файла!\nCSV / JSON")
    write = input("Выйти? (y/n)")
    if write.lower() != 'y':
        menu()
