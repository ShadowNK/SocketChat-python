from socket import *
from _thread import *

# VARIABLES
HOST = '172.08.31.25'  # Direccion IP del seridor
PORT =  50010
server = (HOST, PORT)

device = 0
dev = [] 


def on_new_client(clientsocket,addr):
    global device, dev
    dev.append((clientsocket,addr))
    device += 1
    print ("Conectado con: ", addr)
    while True:
        msg = clientsocket.recv(1024)
        resend_msg(msg, addr)
        
    clientsocket.close()

def resend_msg(msg, ad):
    for i in range(0, device):
        (clientsocket,addr) = dev[i]
        if ad != addr:
            clientsocket.send(msg)

# SOCKET
sock = socket()                 # Create a socket object
sock.bind(server)               # Bind to the port
sock.listen(5)                  # Number of connections


while True:
   conn, addr = sock.accept()     # Establish connection with client.
   start_new_thread(on_new_client,(conn,addr))
sock.close()
