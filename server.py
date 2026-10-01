import socket

HOST = '127.0.0.1'
PORT = 8080

def main():
    # 1. Create the socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Allow port reuse (prevents "Address already in use" errors during dev)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 3. Bind the socket to the IP and Port
    server_socket.bind((HOST, PORT))
    
    # 4. Listen for incoming connections (Queue size of 5)
    server_socket.listen(5)
    print(f"Server is listening on http://{HOST}:{PORT}")
    
    # 5. The Event Loop
    while True:
        # Block and wait for a client to connect
        client_socket, client_address = server_socket.accept()
        print(f"\n--- New Connection from {client_address} ---")
        
        # Read the raw request bytes from the browser (up to 1024 bytes)
        request_data = client_socket.recv(1024).decode('utf-8')
        print(f"Received Raw Request:\n{request_data}")
        
        # Construct the exact string format HTTP requires
        http_response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<html><body><h1>Hello from your custom server!</h1></body></html>"
        )
        
        # Send the response back converted to raw bytes
        client_socket.sendall(http_response.encode('utf-8'))
        
        # Hang up the connection
        client_socket.close()

if __name__ == "__main__":
    main()