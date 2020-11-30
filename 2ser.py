import socket
import threading
import sys
import pickle

host = "127.0.0.1"
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Creado")
sock.bind((host, port))
print ("socket conexion establecida")
sock.listen(1)
print ("socket ahora puede ser escuchado")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('Cliente Conectado {}.'.format(addr))
        conn.send("Cliente conectado".encode('UTF-8'))
        while True:
            datos = conn.recv(1024)
            if datos:
                    print('Recibido: {}'.format(datos))
                
            else:
                print("Cliente desconectado")              
                break
    finally:
        conn.close()
        	
while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()      
    
    

while True:
			msg = raw_input('')
			if msg == 'salir':
				self.sock.close()
				sys.exit()
			else:
				pass




s = Servidor()

