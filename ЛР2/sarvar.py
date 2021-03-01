from logic import StandardLogic
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected ', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
            calc = StandardLogic(a=2.0, b=4.0)
            print(calc.sum())
            conn.sendall(calc.sum())
        yn = input("exit? (y/n)")
        if yn == 'y':
            break
