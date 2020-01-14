from socket import *
from _thread import *

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print (addr[0], ' mensaje: ', msg.decode())
        msg = input('Mensaje para ' + addr[0] + ': ')
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg.encode())
    clientsocket.close()

# VARIABLES
HOST = 'localhost'  # Direccion IP del seridor
PORT =  50025
server = (HOST, PORT)

# SOCKET
sock = socket()                 # Create a socket object
sock.bind(server)               # Bind to the port
sock.listen(5)                  # Number of connections


while True:
   conn, addr = sock.accept()     # Establish connection with client.
   print ("Conectado con: ", addr)
   start_new_thread(on_new_client,(conn,addr))
sock.close()
