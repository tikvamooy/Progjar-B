import sys
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


while True:
    data = sock.recv(512)
    print >>sys.stderr, 'received "%s"' % data
    message = raw_input("ketik pesan: ")
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
