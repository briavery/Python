#class declaration
class Pet():
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    #print details function
    def print_details(self):
        print(f"Kind: {self.kind}, Breed: {self.breed}, Name: {self.name}")

    # Getter functions
    def get_kind(self):
        return self.kind

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name

    # setter functions
    def set_kind(self, kind):
        self.kind = kind

    def set_breed(self, breed):
        self.breed = breed

    def set_name(self, name):
        self.name = name

#function for hasattr()
def checkAttr(obj, attr):
    if hasattr(obj, attr):
        print("Property Exists")
    else:
        print(f"{attr} does not exist in the object")

#Creating class pets
pet1 = Pet("Dog", "Golden Retriever", "Charlie")
pet2 = Pet("Bird", "Macaw", "Annie")
pet3 = Pet("Cat", "Maine Coon", "Leo")

#calling checkAttr function that calls hasattr()
checkAttr(pet1, "name")
checkAttr(pet2, "breed")
checkAttr(pet3, "nothing")

#using the print_details function in the class
pet1.print_details()
pet2.print_details()
pet3.print_details()