import socket
from logic import StandardLogic, ExtendedLogic

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            try:
                data = conn.recv(1024).decode()
                print(f'Приняты данные: {data}')
            except ConnectionAbortedError:
                break
            if not data or data.lower() == 'quit':
                conn.send(b'quit')
            else:
                expr = data.split()
                response = bytes('Неправильное выражение', encoding='utf-8')
                if len(expr) == 3:
                    try:
                        calc = StandardLogic()
                        calc.a = int(expr[0])
                        calc.b = int(expr[2])
                        response = str(calc.calculate(expr[1])).encode()
                    except:
                        pass
                elif len(expr) == 1:
                    try:
                        calc = ExtendedLogic()
                        calc.a = int(expr[0])
                        response = f"{expr[0]} км = {calc.get_miles()} миль".encode()
                    except:
                        pass
                conn.send(response)
