import socket
import sys


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))

selection = 1
while True:
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

    info = str(selection)
    
    if selection == 1:
        name = input("Customer name: ")
        info = info + "," + name
    elif selection == 2:
        name = input("New customer's name: ")
        while not name:
            print("Name cannot be empty, please try again")
            name = input("New customer's name: ")
        info = info + "," + name
        age = input("New customer's age: ")
        info = info + "," + str(age)
        address = input ("New customer's address: ")
        info = info + "," + address
        phone = input("New customer's phone number: ")
        info = info + "," + str(phone)
    elif selection == 3:
        name = input("Customer name to delete: ")
        info = info + "," + name
    elif selection == 4:
        name = input("Enter customer name to update: ")
        info = info + "," + name
        age = input("Customer's updated age: ")
        info = info + "," + str(age)
    elif selection == 5:
        name = input("Enter customer name to update: ")
        info = info + "," + name
        address = input("Customer's updated address: ")
        info = info + "," + str(address)
    elif selection == 6:
        name = input("Enter customer name to update: ")
        info = info + "," + name
        phone = input("Customer's updated phone number: ")
        info = info + "," + str(phone)
    elif selection == 7:
        info = str(7)
    elif selection == 8:
        print("Good bye")
        exit()
    else:
        print("Invalid value. Please enter a valid choice.")
        continue
    sock.sendall(bytes(info +"\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    print("Server Response: {0}\n".format(received))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))