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

   
    filename = client_socket.recv(1024).decode()
    print("File requested:", filename)

    try:
        
        with open(filename, "rb") as file:
            
            file_data = file.read()
            
            client_socket.sendall(file_data)
        print("File sent successfully")
    except FileNotFoundError:
        print("File not found")


    client_socket.close()
