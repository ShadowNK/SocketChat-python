# SocketChat-python

#### NOTA: Asegurarse de que el puerto utilizado y la direccion del servidor sean las mismas en los archivos.
####       Debe utilizar un puerto disponible.
#### Al momento de utilizar primero ejecutar el servidor y luego ellos clientes.

Chat utilizando sockets para comunicacion secuencial.

## Chat 1 - 1 local host

Se tiene que ejecutar en distintos terminales o consolas en un mismo equipo.

## Chat 1 - 1 distintos equipos

Se tiene que comprobar que este la ip del servidor en los dos archivos.

## Chat n - 1 local host

Se tiene que ejecutar en distintos terminales o consolas en un mismo equipo.
La comunicacion es secuencial y de tipo 1 - 1 con el servidor pero varios clientes se pueden conectar a este.

## Chat n - 1 distintos equipos

Se tiene que comprobar que este la ip del servidor en todos los archivos.
La comunicacion es secuencial y de tipo 1 - 1 con el servidor pero varios clientes se pueden conectar a este.

## Chat varios clientes - un servidor local host

Se tiene que ejecutar en distintos terminales o consolas en un mismo equipo.
La comunicacion se maneja mediante hilos con varios clientes y un servidor quien gestiona los mensajes.
#### NOTA: Si se ejecutan muchos clientes se puede colgar el dispositivo.

## Chat varios clientes - un servidor distintos equipos

#### El archivo que tiene que compartir es clienteSocket.py
Se tiene que comprobar que este la ip del servidor en todos los archivos.
La comunicacion se maneja mediante hilos con varios clientes y un servidor quien gestiona los mensajes.
