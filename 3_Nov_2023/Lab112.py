# Take a input from user we will create How

class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details is ", self.color, self.model)

car_color = input("Enter you car Color")
car_model = input("Enter you car Model")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

# Obj ref we can call the function
car_obj_ref.car_details()

# car_details()