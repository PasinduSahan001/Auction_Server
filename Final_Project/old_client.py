import socket
import pickle
import webbrowser

HEADERSIZE = 10

socket_cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cl.connect((socket.gethostname(), 1234))

while True:
    full_msg = b''
    new_msg = True

    while True:
        msg = socket_cl.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            f = open('helloworld.html', 'w')
            dump_msg = pickle.loads(full_msg[HEADERSIZE:])
            print(dump_msg)

            f.write(dump_msg)
            f.close()
            webbrowser.open_new_tab('helloworld.html')
            new_msg = True
            full_msg = b''

    print(full_msg)

