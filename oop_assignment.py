# Assignment: Object-Oriented Programming

# -------------------------
# Activity 1: Design Your Own Class
# -------------------------

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def charge(self):
        return f"{self.brand} {self.model} is charging 🔋"

# Inheritance example
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, waterproof):
        super().__init__(brand, model, battery_life)
        self.waterproof = waterproof

    def fitness_tracking(self):
        return f"{self.brand} {self.model} is tracking your steps 🏃‍♂️"


# -------------------------
# Activity 2: Polymorphism Challenge
# -------------------------

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"


# -------------------------
# Testing the classes
# -------------------------

if __name__ == "__main__":
    # Activity 1
    phone = Smartphone("Samsung", "Galaxy S21", "12 hours")
    watch = Smartwatch("Apple", "Watch Series 7", "18 hours", True)

    print(phone.call("08012345678"))
    print(phone.charge())
    print(watch.fitness_tracking())
    print(watch.charge())

    print("\n--- Polymorphism Challenge ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
