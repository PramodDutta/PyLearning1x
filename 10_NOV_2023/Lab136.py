a = int(input("Enter your A number"))
b = int(input("Enter your B number"))
try:
    c = a/b
    print(c)
except Exception as error:
    print("You are diving the Value of A with zero, Please don't do it", error)
