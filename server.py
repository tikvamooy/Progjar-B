import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12000)
server_address2 = ('localhost', 5000)
print >>sys.stderr, 'starting up on %s port %s' % server_address

print >>sys.stderr, 'starting up on %s port %s' % server_address2
sock.bind(server_address)
sock2.bind(server_address2)
sock.listen(1)
sock2.listen(1)

print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()
connection2, client_address2 = sock2.accept()
print >>sys.stderr, 'connection from', client_address
print >>sys.stderr, 'connection from', client_address2

while True:
    data = connection.recv(512)
    print >>sys.stderr, 'received "%s"' % data
    print >>sys.stderr, 'sending data back to the client'
    connection2.sendall(data)
    data2 = connection2.recv(512)
    print >>sys.stderr, 'received "%s"' % data2
    print >>sys.stderr, 'sending data back to the client'
    connection.sendall(data2)
