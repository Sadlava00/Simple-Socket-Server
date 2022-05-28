import socket

class Server():
    global clients
    clients = []

    def setup(self, port:int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(socket.gethostname())
        sock.bind((ip, port))

        sock.listen(100)

        def messagelisten(connection, address):
            while True:
                msg = connection.recv(2048)
                if msg:
                    print(msg.decode())

        def start():
            while True:
                conn, addr = sock.accept()
                clients.append(conn)
                print(f'[{addr}] Joined!')
                messagelisten(conn, addr)

        print(f'Listening on [IP:{ip}|PORT:{port}]')
        start()

    def showclients(list=bool):
        if list == True or list == 'True':
            print(clients)
        elif list == False or list == 'False':
            for client in clients:
                print(f'[CONNECTION]: {client}')
