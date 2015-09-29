import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


while True:
    message = raw_input ("ketik pesan1: ")
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
    data = sock.recv(512)
    print >>sys.stderr, 'received "%s"' % data
