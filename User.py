class User:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
    
    def display(self):
        print("this is "+ self.name)
        print(self.age)
        print(self.address)
        print(self.phone)