# Collection -

# list, dic, tuple, set, OrderedDict - Data Type

regular = (1, 2, 3)
# regular[0] = 20 # They are not mutable

print(regular[0])

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])



person = Person(name="Pramod", age=34, gender="M")

print("Name", person.name)
print("Age", person.age)
print("Gender", person.gender)


class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name}")


person2 = Person2("Pramod", 23, "M")
person2.print_details()

