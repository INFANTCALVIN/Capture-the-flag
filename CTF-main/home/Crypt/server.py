import socket


def server(host, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Bind the socket to the host and port
            s.bind((host, port))
            # Start listening for incoming connections
            s.listen()
            print(f"Server listening on {host}:{port}")

            # Accept incoming connection
            conn, addr = s.accept()
            print(f"Connected to {addr}")
            message = "ThReAdS_BuStErS{pythonanswerkedachuruchu}"
            conn.sendall(message.encode())

            with conn:
                while True:
                    # Receive data from the client
                    data = conn.recv(1024)
                    if not data:
                        break
                    # Process received data
                    print(f"Received: {data.decode()}")
                    # Example of echoing back the received data
                    conn.sendall(data)
        except KeyboardInterrupt:
            print("Server stopped by user.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    host = "192.168.136.132"  # or your server's IP address
    port = 4444  # choose an appropriate port number
    server(host, port)
