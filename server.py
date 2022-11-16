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
        #print(self.data)

        load()

        data = self.data.decode("utf-8")
        data = data.split(',')
        print(data)
        if (data[0] == "1"):
            response = find(data[1])
            
        
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        
        response_as_bytes = str.encode(response)
        self.request.sendall(response_as_bytes)


#load all users from data.txt 
def separate():
    print()

def load():
    with open("data.txt", "r") as user_data:
        
        for line in user_data:
            #users_list.append(User())
            split = line.split("|")
            newUser = User(split[0],split[1],split[2],split[3])
            users_list.append(newUser)
            
            #newUser.display()

# Option 1            
def find(name):
    try:
        for user in users_list:
            User.display(user)
            if (user.name == name):
                print("FOUND {0}".format(user.name))
                return "FOUND {0}".format(user.name)
    except:
        print("{0} not found in database".format(name))

        

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()