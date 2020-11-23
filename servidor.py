import socket
port = 9000


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.bind(("127.0.0.1", 9000))
print("Esperando Coneccion", port)


sock.listen(1)


con, client_addr = sock.accept()
print("Cliente Conectado.!")
text = "Hola soy el Servidor"
con.send(text.encode())
con.close()
print("... ... ...")
print("Cliente Desconectado.!")

sock.close()
