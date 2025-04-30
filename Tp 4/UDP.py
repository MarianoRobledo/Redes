import socket
import threading

PUERTO=60000

socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try: 
    socket_server.bind(("0.0.0.0",PUERTO))
except OSError as e:
                print(f"Error de conexión: {e}")
finally:
     socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

stop_event= threading.Event()



def escucha():
    while not stop_event.is_set():
        buffer=socket_server.recvfrom(1024)
        msnCompleto=buffer[0].decode()
        ip=buffer[1][0]
        msn=msnCompleto.split(":")
        usuario=msn[0]
        mensaje=msn[1]
        if mensaje=="exit":
            print(f"El usuario {usuario} ({ip}) ha abandonado la conversación")
        elif mensaje=="nuevo":
            print(f"El usuario {usuario} se ha unido a la conversación")
        else:
            print(f"{usuario}({ip})dice: {mensaje}")


def enviar():
    hilo1 = threading.Thread(target=escucha)
    hilo1.start()

    user=input("Dar tu nombre: ")
    msn=user+":nuevo"
    socket_server.sendto(msn.encode(),("255.255.255.255",PUERTO))

    while True:

        user_input=input("->")
        msn=user+":"+user_input

        socket_server.sendto(msn.encode(),("255.255.255.255",PUERTO))

        if user_input.lower()=="exit":
            stop_event.set()
            print("Saliendo de la conversación")            
            break
    hilo1.join()
    socket_server.close

enviar()





