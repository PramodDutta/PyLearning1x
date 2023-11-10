# Method Overloading:
# Python does not support method overloading in the traditional sense
# Same name of a function with different Parameter

class MathUtil:
    def add(self, a, b=0, c=0):
        return a + b + c


math = MathUtil()
# op11 = math.add("pramod")
# op11 = math.add()
op0 =  math.add(1)
op1= math.add(1, 2)
op2 = math.add(1, 2,3)
print(op0)
print(op1)
print(op2)
# math.add(1, 2, 3)  ## Python does not support method overloading in the traditional sense
