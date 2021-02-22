import json
import csv
import os.path
lst = []


def acceptance_criteria(fn):
    def wrapper(obj):
        if obj['fuel_used'] > 0 and obj['cars_count'] > 0:
            fn(obj)
        else:
            print('ban')
    return wrapper


def print_data(data):
    print('D\t\tFU\t\tC\t\tAVG')
    for i in data:
        print(
            f"{i['depot']}\t\t{i['fuel_used']}\t\t{i['cars_count']}\t\t{i['avg_fuel_used']}")


@acceptance_criteria
def add(obj):
    lst.append(obj)


def input_depot():
    for i in range(int(input('Сколько автобаз нужно добавить?'))):
        obj = {}
        obj['depot'] = input('Название автобазы: ')
        obj['fuel_used'] = used = float(input('Топлива потрачено(кг): '))
        obj['cars_count'] = cars = int(input('Количество машин: '))
        obj['avg_fuel_used'] = used/cars
        add(obj)


def save_json(name):
    input_depot()
    with open(name, 'w') as out:
        json.dump(lst, out)
    lst.clear()


def save_csv(name):
    input_depot()
    with open(name, 'w') as out:
        w = csv.DictWriter(out, lst[0].keys())
        w.writeheader()
        for l in lst:
            w.writerow(l)


def load_json(name):
    with open(name, 'r') as read:
        print_data(json.load(read))
