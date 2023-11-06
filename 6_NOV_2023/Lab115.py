# Encapsulation
# Data Members(Attributes) and Methods Together in a class
# Person -> name,age and eat(), sleep()


# Visibility

# !! Public Member
# Public members have no special naming convention in Python and
# are accessible from anywhere.
# They can be accessed directly from outside the class and other modules.


# ----------------------
# !! Protected Member
# Protected members are denoted by a single underscore prefix (_).
# They can still be accessed from outside the class, but it is considered a
# best practice not to do so directly.


# ----------------------
# !! Private  Member
# Private members are denoted by a double underscore prefix (__).
# Private members are intended to be used within the class only.


class MyClass:

    def __int__(self):
        self.public_var = 10
        self._protected_var = 12
        self.__private_var = 15

    def public_method(self):
        print("This is Public Method")



    def _protected_method(self):
        print("This is Protected Method")
        print(self.__private_var)

    def __private_method(self):
        print("This is a private method.")



obj = MyClass()

# Public
obj.public_method()


