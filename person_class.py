class Person:
    def __init__(self, name, address, age, phone_number):
        #Initialize variables for class create
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    #Getter for each data
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone_number(self):
        return self.__phone_number

    #Setter for each data
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

person1 = Person("Briana", "123 St", "22", "1234567890")
person2 = Person("Kevin", "456 St", "23", "0987654321")
person3 = Person("Kier", "789 St", "20", "2811924392")

print(f"Person 1 Info:\nName: {person1.get_name()}, Address: {person1.get_address()}, Age: {person1.get_age()}, Phone #: {person1.get_phone_number()}")
print(f"Person 2 Info:\nName: {person2.get_name()}, Address: {person2.get_address()}, Age: {person2.get_age()}, Phone #: {person2.get_phone_number()}")
print(f"Person 1 Info:\nName: {person3.get_name()}, Address: {person3.get_address()}, Age: {person3.get_age()}, Phone #: {person3.get_phone_number()}")