# Recovered student coursework; see README.md and PROVENANCE.json for attribution and status.
from pathlib import Path
import csv
import sys
import socket
import threading

#Youtube video used "https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim"
SERVER = '127.0.0.1'

# Airport lookup with IP and Port mappings
AIRPORT_LOOKUP = {
    'ANC': (SERVER, 8080),  # Anchorage (HUB)
    'SEA': (SERVER, 8081),  # Seattle (HUB)
    'FAI': (SERVER, 8082),  # Fairbanks
    'BRW': (SERVER, 8083),  # Barrow
    'DLG': (SERVER, 8084),  # Dillingham
    'ADQ': (SERVER, 8085),  # Kodiak
    'AKN': (SERVER, 8086),  # King Salmon
    'JNU': (SERVER, 8087),  # Juneau
    'OME': (SERVER, 8088),  # Nome
    'GEG': (SERVER, 8089),  # Spokane
}

# Hub Class
class Hub:
    def __init__(self, name):
        self.name = name
        self.server_ip, self.server_port = AIRPORT_LOOKUP[name]
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_ip, self.server_port))
        self.server_socket.listen(10)
        print(f"{self.name} (HUB ACTIVE) {self.server_ip}:{self.server_port}")

    def client(self, client_socket, client_address):
        try:
            data = client_socket.recv(1024)
            if data:
                passenger = Passenger.string(data.decode())
                print(f"{passenger} has arrived at {self.name}")
                if passenger.destination == self.name:
                    # Passenger has reached their destination
                    ack = f"[{self.name}] {passenger.name} has arrived at their destination: {self.name}"
                    print(ack)
                    
                elif passenger.layover == self.name:
                    # Passenger is at layover, route to final destination
                    ack = f"[{self.name}] {passenger.name} layover at {self.name}, routing to {passenger.destination}"
                    print(ack)

            client_socket.sendall(ack.encode())
                
        except Exception as e:
            print(f"{e}")
        finally:
            client_socket.close()
            print(f"Connection closed by {client_address}")





    #Used ChatGPT for threading - wasnt sure how to thread in python
    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            client_thread = threading.Thread(target=self.client, args=(client_socket, client_address))
            client_thread.start()


# Spoke Class
class Spoke:
    def __init__(self, name):
        self.name = name

        self.spoke_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def flytohub(self, hub_name):
            try:
                # Ensure the hub is either ANC or SEA
                if hub_name in ['ANC', 'SEA']:
                    self.hub_ip, self.hub_port = AIRPORT_LOOKUP[hub_name]
                    print(f"Attempting to connect to hub {hub_name} at {self.hub_ip}:{self.hub_port}")
                    self.spoke_socket.connect((self.hub_ip, self.hub_port))
                    print(f"{self.name} (SPOKE) connected to {self.hub_ip}:{self.hub_port}")
            except Exception as e:
                print(f"flytohub: {e}")

    def send(self, csv_file):
        try:
            passengers = Passenger.csv(csv_file)
            for passenger in passengers:
                if passenger.source == self.name:
                    # Fly to the layover hub first (SEA or ANC)
                    if passenger.layover == 'SEA' or passenger.destination == 'SEA':
                        # Fly to SEA first
                        print(f"Sending {passenger.name} to SEA hub")
                        self.flytohub('SEA')
                    else:
                        # Fly to ANC if no layover or layover is ANC
                        print(f"Sending {passenger.name} to ANC hub")
                        self.flytohub('ANC')
                    message = str(passenger)
                    self.spoke_socket.sendall(message.encode())
                    print(f"Sent passenger data: {message}")
                    ack = self.spoke_socket.recv(1024).decode()
                    print(f"Received acknowledgment: {ack}")
        except Exception as e:
            print(f"sendfromcsv: {e}")

    def close_connection(self):
        self.spoke_socket.close()
        print(f"Spoke {self.name} disconnected from hub")

# Passenger Class
class Passenger:
    def __init__(self, name, source, destination, layover=''):
        self.name = name
        self.source = source
        self.destination = destination
        self.layover = layover

    def __str__(self):
        return f"{self.name},{self.source},{self.destination},{self.layover or 'None'}"

    
    def string(data):
        parts = data.split(',')
        name, source, destination, layover = parts[0], parts[1], parts[2], parts[3]
        if layover == 'None':
            layover = ''
        return Passenger(name, source, destination, layover)

    
    def csv(passengerfile):
        passengers = []
        with open(passengerfile, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                passengers.append(Passenger(*row))
        return passengers



#Main Function to Run Hubs or Spokes
# sys commands use from "https://www.geeksforgeeks.org/python-sys-module/"
if __name__ == "__main__":
    airportType = sys.argv[1].upper()
    airport_code = sys.argv[2].upper()

    # Change the CSV file path to your file location here:
    csv_file = Path(__file__).with_name("passengers.example.csv")

    if airportType == "HUB":
        hub = Hub(airport_code)
        hub.start()
    elif airportType == "SPOKE":
        spoke = Spoke(airport_code)
        
        if(airport_code == 'GEG'):
            spoke.flytohub('SEA')  #STUCK HERE - WILL NOT CONNECT TO SEA UNLESS SEA IS HARDCODED? - THIS CONDITION IS NEVER TRUE...
        else:
            spoke.flytohub('ANC')  

        spoke.send(csv_file)
        spoke.close_connection()
    else:
        print("Invalid. ENTER: 'HUB' or 'SPOKE' THEN THE AIRPORT LIKE: HUB ANC.")
