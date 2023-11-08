# Parent - Child
# Father -> son
# GF -> F -> S
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:

    def car(self):
        print("Lambo")
    def speak(self):
        print("Animal Speak!")


class Dog(Animal):
    pass



dog = Dog()
dog.speak()
