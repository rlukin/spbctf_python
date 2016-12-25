import socket


def solve(a, b):
    sock = socket.socket()
    sock.connect((a,b))
    for i in range(100):
        data = sock.recv(50000)
        print(data)
        c = str(eval(data))
        sock.send(c.encode('ascii'))
    return 0
