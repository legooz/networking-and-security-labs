# Recovered student coursework; see README.md and PROVENANCE.json for attribution and status.
import socket

# Create a TCP object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

# Listen for incoming connections.
# You can specify a maximum number of clients in the queue. 5 here.
server_socket.listen(5)
print("Server is listening on {}:{}".format(*server_address))
counter = 0
while True:
    # Wait for a connection from a client
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(*client_address))
    
    try:
        while counter < 3:
            # Receive data from the client
            client_socket.settimeout(10)
            data = client_socket.recv(1024)
            if not data:
                break  # No more data, break the loop
  
            # Decode the received data, format with the variables involved, and display the string.
            print(f"Received data from {client_address}: {data.decode()}")
    
            # Create an acknowledgment.
            ack = "Hey, this is the server acknowledging the receipt of your data: " + data.decode()

            # Encode the acknowledgment and send to client.
            client_socket.sendall(ack.encode())
    except Exception as e:
        print("Error: {}".format(e))
        counter+=1
        print("timeout occurred counter:", counter)
        print("Connection closed by {}:{}".format(*client_address))
client_socket.close()
