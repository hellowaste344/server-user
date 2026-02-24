class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def get_model(self):
        return self.model


print(Car("Toyota", 2022).get_model())
