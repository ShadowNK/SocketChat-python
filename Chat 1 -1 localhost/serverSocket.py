from socket import *
# Creating a server socket on local machine

# VARIABLES
HOST = 'localhost'  # Direccion IP del seridor
PORT =  5000

# Socket
sock = socket(AF_INET, SOCK_STREAM)
sock.bind( (HOST, PORT) )
sock.listen(1)

# Establecer la coneccion
conn, addr = sock.accept()
print ("Conectado con: ", addr)

# Comunicacion
while True:
    data = conn.recv(1024)
    print ("Recivido: ", repr(data.decode()))
    reply = input("Respuesta: ")
    conn.sendall(reply.encode())
    print ("Esperando respuesta ...")

# Cerrar la coneccion
conn.close()
