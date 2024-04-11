class Employee():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    #getter functions
    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    #setter functions
    def setName(self, name):
        self.name = name

    def setNumber(self, number):
        self.number = number

class ProductionWorker(Employee):
    def __init__(self, name, number, shiftNum, pay):
        super().__init__(name, number)
        self.shiftNum = shiftNum
        self.pay = pay

    #getter functions
    def getShiftNum(self):
        return self.shiftNum

    def getPay(self):
        return self.pay

    #setter functions
    def setShiftNum(self, shiftNum):
        self.shiftNum = shiftNum

    def setPay(self, pay):
        self.pay = pay

print("Enter the following details of the Employee")
print("----------------------------------------------")
name = input("Enter Employee Name: ")
num = input("Enter Employee Number: ")
pay = input("Enter Pay Rate: ")
shiftNum = input("Enter Shift Number: ")
print("------------------------------------------------------")

worker = ProductionWorker(name, num, pay, shiftNum)

print("Details of Employee: ")
print("------------------------------------------------------")
print("Name:", worker.name)
print("Employee Number:", worker.number)
print("Shift:", worker.shiftNum)
print("Pay Rate:", worker.pay)