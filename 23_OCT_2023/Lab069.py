# def sayHello():
#     print("Hello")
#
# sayHello()
#
#
# def funcWithParam(a):
#     return a**2
#
# o = funcWithParam(2)
# print(o)

# Lambda Expression -> Now copied by the Java


# def doubleOfMe(value):
#     return value*2


output = lambda value:value*2
print(output(2))


def sayHello(name):
    print("Hi your name is ",name)


sayHelloLambda = lambda name: print("Hi your name is ", name)

sayHello("Pramod")

sayHelloLambda("Lucky")