import socket
from logging import send
log = ['SLAVA UKRAINE']

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Установлено соединение с сервером: {HOST}:{PORT}')
    while True:
        print("Выберите действие\n")
        print("1. Обычный калькулятор")
        print("2. Расшеренный калькулятор")
        print("3. Выйти")
        action = input()
        if action == "1":
            inp = input("Введите выражение\n").encode()
            if len(inp.split()) != 3:
                print("Некорректное выражение!")
                continue
            log.append(f'Slava Ukraini! Користувач ввiв {inp.decode()}')
            s.send(inp)
        elif action == "2":
            inp = input("Введите значение\n").encode()
            if len(inp.split()) != 1:
                print("Некорректное выражение!")
                continue
            log.append(f'Slava Ukraini! Користувач ввiв {inp.decode()}')
            s.send(inp)
        elif action == "3":
            send(log)
            break
        else:
            print("Некорректное значение!")
            continue
        data = s.recv(1024).decode()
        print('Ответ от сервера:', data)
        log.append(f'Slava Ukraini! Прийшла вiдповiдь вiд сервера {data}')
