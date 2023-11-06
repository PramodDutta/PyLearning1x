class Person:

    def __init__(self):
        print("Can I use you?")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You created an Object with name and age")

    def printDetails(self):
        print("Your details are", self.name, self.age)

    def printDetails2(self):
        print("Your details are", self.name * 2)


amit = Person("amit", 34)
amit.printDetails()

nikhil = Person("nikhil", 45)
nikhil.printDetails()
