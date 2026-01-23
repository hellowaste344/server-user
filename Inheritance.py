class Dog:
    def __init__(self, name):
        self.name = name
        
    def display_name(self):
        print(f"dog's name: {self.name}")

class Labrador(Dog): # Single Inheritance
    def sound(self):
        print("Labrador woofs")
        
class GuideDog(Labrador):# Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way")
        
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):# Multiple Inheritance
    def sound(self):
        print("Golden Retreiver barks")
        
        
lab = Labrador("buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()