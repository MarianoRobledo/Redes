import socket
import threading

PUERTO=60000


stop_event= threading.Event()

        

def recibirCliente():
     while not stop_event.is_set():
        msg = socket_cliente.recv(100).decode("utf-8")
        
        print(f"Mensage: {msg}")

def envioCliente():
    hilo_recibir_Servidor = threading.Thread(target=recibirCliente)
    hilo_recibir_Servidor.start()
    
    while True:
        msg=input("-->")
        socket_cliente.send(msg.encode())
        if msg=="exit":
            stop_event.set()
            break
    socket_cliente.close()




def envioServidor():    
    while not stop_event.is_set():
        msg=input("-->")
        if msg=="exit":
            print("No se puede salir porque estas en una conexion")
            so.send(msg.encode())
        elif msg=="ffgg83":
            break
        else:
            so.send(msg.encode())
        
        
def recibirServidor():   
    hilo_envio_servidor = threading.Thread(target=envioServidor)
    hilo_envio_servidor.start() 
    while not stop_event.is_set():
        msg = so.recv(100).decode("utf-8")
        if msg=="exit":
                print("Ha abandonado la conversación")
                so.send("ffgg83")
                stop_event.set()                
                break
        else:
            print(f"Mensage: {msg}")
    stop_event.clear()
    so.close


    
        




user_name=input("Dar tu nombre: ")
flag=True
while flag:
    print("Seleccionar modo \ 1- Enviar mensaje \ 2- Esperar mensaje")
    res=input()
    if res=="1" or res=="2":
        flag=False

match res:
    case "1": #cliente
        socket_cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_cliente.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #socket_server.bind(("0.0.0.0",PUERTO))
        #socket_cliente.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #socket_server.listen(2)

        flag=True
        while flag:
            try:
                ip=input("Dar una IP: ")
                socket_cliente.connect((ip, PUERTO))  # IP o puerto inexistente
                print("Se ha conectado")
                #activar cada hilo para la conversacion
                envioCliente()
            except socket.gaierror:
                print("Dirección IP o nombre de host no válido.")
            except ConnectionRefusedError:
                print("Conexión rechazada: el puerto no está escuchando.")
            except socket.timeout:
                print("Tiempo de espera agotado al intentar conectar.")
            except OSError as e:
                print(f"Error de conexión: {e}")
            finally:
                print("Quiere volver a intenerar o establecer otra conexion" \
                "1- Si " \
                "2- No")
                res=input()
                if res=="2":
                    flag=False

    case "2": #servidor
        socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_server.bind(("0.0.0.0",PUERTO))
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        socket_server.listen(1)
        while True:
            so=None
            print("Esperando conexion")
            so,ip=socket_server.accept()
            recibirServidor()  
            res=None  
            res=input("Quieres Continuar? 1=si, 2=no ")
            if res=="2":
                print("Has finalizado el servidor.")
                socket_server.close                
                break
            so.close
        print("Has finalizado el servidor.")
            
        


