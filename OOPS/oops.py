class Car:
    totalCar=0
    def __init__(self,brand,model) -> None:
        self.__brand=brand # privatization
        self.__model=model
        Car.totalCar+=1
    
    # Method
    def fullName(self):
        return f'{self.__brand} - {self.__model}'
    
    def get_brand(self):
        return self.__brand + "!"
    
    # Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are vehicles"
    
    @property
    def model(self):
        return self.__model
        


# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,batterySize):
        self.batterySize=batterySize
        super().__init__(brand,model)

    def batterySize(self):
        return f"Your battery size is {self.batterySize}"
    
    def fullName(self):
        print("Running in between...")
        return super().fullName()
    
    # Polymorphism
    def fuel_type(self):
        return "Electric charge"


myCar=Car("Toyota","Corolla")
myElectricCar=ElectricCar("Toyota","Corolla","100")



# Multiple Inheritance
class Battery:
    def batteryInfo(self):
        return "Battery Info"

class Engine:
    def engineInfo(self):
        return "Engine Info"

class ElectricCarTwo(Battery,Engine,Car):
    pass

myNewTesla = ElectricCarTwo("Tesla","Model 3")
print(myNewTesla.batteryInfo())
print(myNewTesla.engineInfo())

"""
Constructor: Constructor is used to initialize the objectself
Method: A function associated with the class
Polymorphism: Method Overriding - child class method overriding the parent class
Inheritance: A class inherits the attributes and methods from another class
Encapsulation: Data hiding. Ex - __brand
Static Method: A class method which can be called without creating an object
Read-Only Property: A property that cannot be modified.
Multiple Inheritance: A class can inherit from multiple classes
"""