import socket

HOST, PORT = '0.0.0.0', 8888

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))
serversocket.listen(1)
print 'Serving HTTP on {}:{}'.format(HOST, PORT)

while True:
    conn, addr = serversocket.accept()
    request = conn.recv(1024)
    print request

    response = """\
HTTP/1.1 200 OK

Toy Server
"""
    conn.sendall(response)
    conn.close()