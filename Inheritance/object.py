class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car brand: {self.brand}, Model: {self.model}")

my_car = Car("Toyota", "Mahindra")

my_car.display()
