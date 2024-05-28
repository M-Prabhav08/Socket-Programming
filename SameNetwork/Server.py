import socket
import os


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
       
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address

def get_file_metadata(filename):
    file_size = os.path.getsize(filename)
    last_modified = os.path.getmtime(filename)
    file_metadata = "Filename: {}\nSize: {} bytes\nLast Modified: {}".format(filename, file_size, last_modified)
    return file_metadata


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = get_ip_address()
port = 12345


server_socket.bind((host, port))


server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))


files = ["f1.txt", "f2.txt", "f3.txt"]  

while True:
 
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    
    file_list = "\n".join(files)
    client_socket.sendall(file_list.encode())

    
    filename = client_socket.recv(1024).decode()
    print("File requested:", filename)

    try:
       
        with open(filename, "rb") as file:
            
            file_data = file.read()
          
            client_socket.sendall(file_data)
        print("File sent successfully")
    except FileNotFoundError:
        print("File not found")
        client_socket.sendall(b"")  

   
    client_socket.close()
