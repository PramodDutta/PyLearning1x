# Class and Object in Python.

# Person
# Attributes - name,age, phone_no, height, weight, gender, prof
# Methods - Can do -> Run(), sleep(). sing(), talk(), eat(), fight(), learn(), hear(), think()


# Objects
# Amit
# Durga - GENDER  - fEMALE
# Santosh -

class Person:
    # Attributes
    name = None
    age = None
    phone_no = None
    height = None
    weight = None
    gender = None
    prof = None

    # Methods
    def talk(self):
        print("Talk")

    def sleep(self):
        print("Sleep")

    def walk(self):
        return "I am walking"


amit_object = Person()
amit_object.name = "Amit"
amit_object.age = 59
amit_object.phone_no = "987654321"

print(amit_object)
amit_object.sleep()

durga_obj = Person()
durga_obj.name = "Durga"

print(durga_obj)
durga_obj.sleep()