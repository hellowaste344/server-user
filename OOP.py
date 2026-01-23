class Vehicle:
    def __init__(self, brand, year=2025, speed=100):
        self.brand = brand # public attribute
        self._year = year # protected attribute
        self.__speed = speed # private attribute
        
    def get_info(self):
        print(f"Model of {self.brand} in {self._year} goes at speed of {self.__speed}")
        
    # Getter and Setter for private attributes
    def get_year(self):
        return self._year
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        if speed < 0:
            return ValueError("speed cannot be negative!")
        self.__speed = speed

class Car(Vehicle):
    def __init__(self, brand, year, speed, type):
        super().__init__(brand, year, speed) #Calls Vehicle's __init__
        self.type = type

#multilevel class hierarchy
class Mammal:
    def __init__(self, name):
        print(name, "is a mammal")
class CanFly(Mammal):
    def __init__(self, name):
        print(name, "cannot fly")
        super().__init__(name)
class CanSwim(CanFly):
    def __init__(self, name):
        print(name, "cannot swim")
        super().__init__(name)
class Animal(CanSwim):
    def __init__(self, name):
        super().__init__(name)
        
dog = Animal("Dog")

c1 = Vehicle("Tesla Cyber-Truck", 2025, 200)
c1.get_info()
print(c1.brand)
c1.set_speed(250)
print(c1.get_speed())

obj = Car("Cyber-Skeleton", 2025, 350, "Robot")
print(obj.brand, obj.get_year(), obj.get_speed(), obj.type)