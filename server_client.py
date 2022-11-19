import socket

sock = socket.socket()

ip = '127.0.0.1'
port = 4444

sock.connect((ip, port))
print('client started!')
file_name = input('file_name: ')
while True:
    with open(file_name, "r") as f:
        sock.send(f.read().encode('utf-8'))

    data = sock.recv(1024).decode('utf-8')
    if data == 'DONE_':
        sock.close()
        print('done sended! CLOSING CONNECTION!!!')
        break
    else:
        print('ERRORED SENDED!!! TRYING AGAIN? (Y/n)')
        if input('>>> ') == 'Y':
            continue
        else:
            break
