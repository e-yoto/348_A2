class User:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
    
    def display(self):
        print("{0}|{1}|{2}|{3}".format(self.name,self.age,self.address,self.phone))