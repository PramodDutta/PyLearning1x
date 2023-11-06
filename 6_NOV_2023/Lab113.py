class Car:
    name = "Pramod" # Class Varaible

    def __init__(self,make,model): # Default con
        self.make = make  #  Instance Vairable
        self.model = model # Instance Vairable
        print("I will be called first")

    def start_engine(self):
        print("Starting a car", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine()
car2.start_engine()

print(id(car1))
print(id(car2))


# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them