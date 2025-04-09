# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Inherited class to demonstrate polymorphism or encapsulation
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    def info(self):
        super().info()
        print(f"Refresh Rate: {self.refresh_rate}Hz - Great for gaming!")

phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone1.info()
phone1.call("John")

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 144)
gaming_phone.info()
gaming_phone.call("Alex")


class Animal:
    def move(self):
        print("The animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐶.")

class Bird(Animal):
    def move(self):
        print("The bird flies 🐦.")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟.")

animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
