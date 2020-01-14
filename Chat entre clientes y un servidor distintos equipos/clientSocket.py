from socket import *
from _thread import *
# Creating a clientsocket

# Variables
HOST = '172.08.31.25'  # Direccion IP del servidor
PORT = 50010
server = (HOST, PORT)

# Crear el socket
sock = socket(AF_INET, SOCK_STREAM)

# Establecer coneccion
sock.connect(server)

def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def reciver():
    reply = sock.recv(1024)
    print ("Recivido: \n", repr(reply.decode()))


def sender():
    message = input("Mensaje: ")
    message = get_ip() + ': ' + message+ '\n'
    sock.send(message.encode())
    

# Comunicacion
while True:
    start_new_thread(sender,())
    start_new_thread(reciver,())

# Cerrar coneccion
sock.close()
