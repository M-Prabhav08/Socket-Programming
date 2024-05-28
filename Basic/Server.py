import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 12345


server_socket.bind((host, port))


server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:
    
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    while True:
       
        data = client_socket.recv(1024)
        if not data:
            break

        print("Received:", data.decode())

        
        client_socket.sendall(data)

   
    client_socket.close()
