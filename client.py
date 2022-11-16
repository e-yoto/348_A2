import socket
import sys
import User


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

def showMenu():
    print("""Python DB Menu
1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address
6. Update customer phone
7. Print report
8. Exit
    """)
    selection = int(input("Select: "))
    
    if (selection >= 1 and selection <= 8):
        

        if selection == 1:
            info = str(selection)
            name = input("Customer name: ")
            info = info + "," + name
            sock.sendall(bytes(info +"\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    showMenu()
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

# print("Sent:     {}".format(data))
# print("Received: {}".format(received))