import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345


client_socket.connect((host, port))


filename = input("Enter filename to request: ")

client_socket.sendall(filename.encode())


file_data = client_socket.recv(1024)

if file_data:
   
    with open("received_" + filename, "wb") as file:
        file.write(file_data)
    print("File received successfully")
else:
    print("File not found on server")


client_socket.close()
