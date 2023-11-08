# Single Inheritance - 90%
# Use the properties, variables and methods of your base class or parent class by the sub class or son class




class Father:
    bank_bal =  100

    def one_bhk(self):
        print("Use it son")


class Son(Father):
    pass # I wil write the code in future!! Skip


s = Son()
s.one_bhk()
print(s.bank_bal)