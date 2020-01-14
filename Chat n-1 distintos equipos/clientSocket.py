from socket import *
# Creating a clientsocket

# Variables
HOST = '172.31.108.21'  # Direccion IP del servidor
PORT = 50000
server = (HOST, PORT)

# Crear el socket
sock = socket(AF_INET, SOCK_STREAM)

# Establecer coneccion
sock.connect(server)

# Comunicacion
while True:
    message = input("Mensaje: ")
    sock.send(message.encode())
    print ("Esperando respuesta ...")
    reply = sock.recv(1024)
    print ("Recivido: ", repr(reply.decode()))
    
# Cerrar coneccion
sock.close()
