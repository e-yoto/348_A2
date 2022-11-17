class User:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
    
    def display(self):
        print("{0}|{1}|{2}|{3}".format(self.name,self.age,self.address,self.phone))
    
    def get_user(self):
        return "{0}|{1}|{2}|{3}".format(self.name,self.age,self.address,self.phone)
    
    def update_age(self, age):
        self.age = age
        
    def update_address(self,address):
        self.address = address
    
    def update_phone(self,phone):
        self.phone = phone