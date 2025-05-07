import socket
import threading
import os


PUERTO=60000
        


def recv_all(filesize):
    received = b''
    while len(received) < filesize:
        chunk = socket_cliente.recv(4096)
        if not chunk:
            break  # connection closed
        received += chunk
    return received
        

def envioCliente():
    cwd =os.getcwd()
    print(cwd)
    nombreArchivo=socket_cliente.recv(256).decode("utf-8")
    nom=nombreArchivo.split(":")
    nombre=nom[0]
    print(nombre)
    sizeByte = socket_cliente.recv(4)
    size =int.from_bytes(sizeByte, byteorder="little")
    print(size)
    with open(nombre, 'wb') as f:
        file_data = recv_all(size)
        f.write(file_data)




cwd =os.getcwd()
print(cwd)
try:
    socket_cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_cliente.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip=input("Dar una IP: ")
    socket_cliente.connect((ip, PUERTO))  # IP o puerto inexistente
    print("Se ha conectado")
    
    #activar cada hilo para la conversacion
    envioCliente()
    print("hola")
except socket.gaierror:
    print("Dirección IP o nombre de host no válido.")
except ConnectionRefusedError:
    print("Conexión rechazada: el puerto no está escuchando.")
except socket.timeout:
    print("Tiempo de espera agotado al intentar conectar.")
except OSError as e:
    print(f"Error de conexión: {e}")


 
            
        


