import socket
import pickle
import webbrowser


HEADERSIZE = 10

IP = '127.0.0.1'
PORT = 1234

socket_01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_01.bind((IP, PORT))
socket_01.listen()


while True:
    clientsocket, address = socket_01.accept()
    t = clientsocket.recv(1024)
    try:
        filename = t.split()[1]
        x = []
        x.append(filename.decode('ascii'))
        y = x[0][1:]
        print(y)
        final = y.find("email")
        # if "home" in y:
        #     webbrowser.open(y)
        if "email" in y:
            print("Gammac Thamai")
    except:
        pass




    print(f"lol {address}")

    dump_msg = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""
    msg = pickle.dumps(dump_msg)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(bytes(msg))


# while True:
#     clientsocket, address = socket_01.accept()
#     print(f"lol {address}")


#     msg =  """<html>
# <head></head>
# <body><p>Hello World!</p></body>
# </html>"""
#     msg = f'{len(msg):<{HEADERSIZE}}' + msg

#     clientsocket.send(bytes(msg, "utf-8"))

