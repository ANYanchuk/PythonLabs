import json
import os
from tabulate import tabulate


def validate_data(process_func):
    def arguments_wrapper(self, input_line: str):
        processed_data = input_line.split(',')
        if len(processed_data) != 3:
            print('Слишком мало значений!')
        elif not processed_data[0] or processed_data[0].strip().isdigit():
            print('Фамилия некорректна!')
        elif not processed_data[1].strip().isdigit() or not processed_data[2].strip().isdigit():
            print('Значение удержаных или выданных денег некорректно!')
        else:
            return process_func(self, input_line)

    return arguments_wrapper


class JsonManager(object):
    def process_file(self):
        processes = {'r': self.process_reading, 'w': self.process_writing}
        process = input('\033[38mВыберите режим : чтение(r) / запись(w)\n')
        if process and process in processes:
            file = input('\033[38mВведите путь к файлу\n')
            processes[process.lower()](file)

    def process_writing(self, file):
        if file.endswith('.json'):
            if not os.path.exists(file):
                open(file, 'a').close()
            with open(file) as read_file:
                file_data = json.load(read_file) if os.stat(file).st_size else []
            with open(file, 'w') as output_file:
                print('Вводите данные через запятую в порядке:')
                print("Автобаза, Витрачено палива, кг., Кiлькiсть автомашин")
                result_data = []
                table_data = []
                while input_string := input():
                    parsed_data = self.parse_input(input_string)
                    if parsed_data:
                        result_data.append(parsed_data)
                        table_data.append(input_string.split(',') + [parsed_data['avg']])
                write_table = tabulate(table_data,
                                       headers=['Автобаза', 'Витрачено палива, кг.', 'Кiлькiсть автомашин', 'Витрачено у середньому'])
                while write := input(f'{write_table}\nЗаписать выбранные данные?(Y/n)\n'):
                    if write.lower() == 'y':
                        if file_data:
                            output_file.write(json.dumps(file_data + result_data))
                        else:
                            output_file.write(json.dumps(result_data))
                        print('Запись в файл окончена')
                        break
                    elif write.lower() == 'n':
                        print('Запись в файл отменена')
                        break
        else:
            print('\033[31mФайл должен иметь разрешение .json')
            self.process_file()

    @validate_data
    def parse_input(self, input_line: str):
        parsed_data = [i.strip() for i in input_line.split(',')]
        return {'depot_name': parsed_data[0], 'fuel_used': float(parsed_data[1]), 'count': float(parsed_data[2]),
                'avg': float(parsed_data[1]) / float(parsed_data[2])}

    def process_reading(self, file):
        if not file.endswith('.json'):
            print('\033[31mФайл должен иметь разрешение .json')
        elif not os.path.exists(file):
            print('\033[31mФайл не существует')
        else:
            self._print_file_data(file)

    @staticmethod
    def _print_file_data(file):
        result_data = []
        rows = int(input('\033[38mВведите количество выводимых строк\n'))
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            for idx, val in enumerate(data):
                if idx <= rows - 1:
                    result_data.append([val['depot_name'], val['fuel_used'], val['count'], val['avg']])
                else:
                    break
            print(tabulate(result_data, headers=['Автобаза', 'Витрачено палива, кг.', 'Кiлькiсть автомашин', 'Витрачено у середньому']))


def process_csv():
    print('CSV обработан')
