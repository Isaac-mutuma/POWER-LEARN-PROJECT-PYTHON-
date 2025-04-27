# vehicles_polymorphism.py

class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path 🚲")

# Example usage
def main():
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()
