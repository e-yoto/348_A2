import socketserver
import User
from User import User
users_list = []
class MyTCPHandler(socketserver.BaseRequestHandler):
    
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))

        data = self.data.decode("utf-8")
        data = data.split(',')
        print("Request data: {0}".format(data))
        response = "INVALID"
        if (data[0] == "1"):
            response = find(data[1])
        elif(data[0]) == "2":
            response = add(data)
        elif(data[0] == "3"):
            response = delete(data[1])
        elif(data[0] == "4"):
            response = update_age(data[1],data[2])
        elif(data[0] == "5"):
            response = update_address(data[1],data[2])
        elif(data[0] == "6"):
            response = update_phone(data[1],data[2])
        elif(data[0] == "7"):
            response = generate_report()
        elif(data[0] == "9"):
            printall()
            
        response_as_bytes = str.encode(response)
        self.request.sendall(response_as_bytes)

#load all users from data.txt 
def load():
    with open("data.txt", "r") as user_data:
        
        for line in user_data:
            split = line.split("|")
            if not split[0]:
                continue
            newUser = User(split[0],split[1],split[2],split[3])
            users_list.append(newUser)

# Option 1            
def find(name):
    for user in users_list:
        if (user.name == name):
            print("FOUND {0}".format(user.name))
            
            return User.get_user(user)
    return "{0} not found in database".format(name)

#Option 2
def add(new_user):
    for user in users_list:
        if (user.name == new_user[1]):
            return "Customer already exists"
    newUser = User(new_user[1],new_user[2],new_user[3],new_user[4])
    users_list.append(newUser)
    return "Customer has been added"

#Option 3
def delete(name):
    for user in users_list:
        if (user.name == name):
            users_list.remove(user)
            return "Customer has succesfully been deleted"
    return "Customer does not exist"

#Option 4
def update_age(name, new_age):
    for user in users_list:
        if (user.name == name):
            User.update_age(user, new_age)
            return "{0}'s age has succesfully been updated".format(name)
    return "Customer does not exist"

#Option 5
def update_address(name, new_address):
    for user in users_list:
        if (user.name == name):
            User.update_address(user, new_address)
            return "{0}'s address has succesfully been updated".format(name)
    return "Customer does not exist"

#Option 6
def update_phone(name, new_phone):
    for user in users_list:
        if (user.name == name):
            User.update_phone(user, new_phone)
            return "{0}'s phone has succesfully been updated".format(name)
    return "Customer does not exist"

#Option 7
def generate_report():
    sorted_list = sorted(users_list, key=lambda user: user.name)
    report = "\n** Python DB contents\n"
    for user in sorted_list:
        report += User.get_user(user) + "\n"
    sorted_list = []
    return report

def printall():
    print(len(users_list))
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    load()
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()