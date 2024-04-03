class Pet:
    #Class variables
    vet_name = "Vet Name"

    #initializer
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type

    #Getter functions
    def get_owner_first_name(self):
        return self.owner_first_name
    def get_owner_last_name(self):
        return self.owner_last_name
    def get_pet_id(self):
        return self.pet_id
    def get_pet_name(self):
        return self.pet_name
    def get_pet_type(self):
        return self.pet_type

    #setter functions
    def set_owner_first_name(self, first_name):
        self.owner_first_name = first_name
    def set_owner_last_name(self, last_name):
        self.owner_last_name = last_name
    def set_pet_id(self, pet_id):
        self.pet_id = pet_id
    def set_pet_name(self, pet_name):
        self.pet_name = pet_name
    def set_pet_type(self, pet_type):
        self.pet_type = pet_type

    #Display info
    def display_pet_info(self):
        print(f"Owner Name: {self.owner_first_name} {self.owner_last_name}, Pet ID: {self.pet_id}, Pet Name: {self.pet_name}, Pet Type: {self.pet_type}")

def check_property(pet, property):
    if hasattr(pet, property):
        print("Property Exists")
    else:
        print(f"{property} does not exist in the object")

pet1 = Pet("Briana", "Avery", "01", "Max", "Dog")
pet2 = Pet("Kevin", "Dai", "02", "Winter", "Hamster")
pet3 = Pet("Kalyn", "Dai", "03", "Leo", "Cat")

#uses a set function
pet3.set_pet_name("Maize")

#displays data for each pet
pet1.display_pet_info()
pet2.display_pet_info()
pet2.display_pet_info()

#uses check property
check_property(pet1, "nonexistant_object")
check_property(pet3, "pet_id")