# Abstraction - OOPs
# Hiding the details and showing the what is required

# Car ->  start the engine ->  put the gear -> start driving
# -> Do you know How engine is started? , How gear box was managed?
# hide the implementation and show only the important details


# to represent complex systems by simplifying and hiding unnecessary details

# ABC -> ? Abstract Base Class
# Abstract base Methods

# Shape -> Rectangle, Circle
# Shape -> perimeter, area

# Animal(speak) -> Dog, Cat, Toger( roar)

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bow Bow"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Tiger(Animal):
    def sound(self):
        return "Roar Roar!!, Grrrr!!!"


dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())

tiger= Tiger()
print(tiger.sound())


# animal = Animal()