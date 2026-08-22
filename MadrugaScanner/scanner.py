import socket

HOST = "0.0.0.0"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Waiting for Connection...")
    conn, addr = server_socket.accept()

    with conn:
        print(f"Connected with {addr}")
        while(True):
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        
