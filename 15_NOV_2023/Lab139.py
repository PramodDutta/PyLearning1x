# try except
# try:
#     a = 10 / 0
# except ZeroDivisionError as e:
#     print(e)

# try except and nested except
try:
    num1 = int(input("Enter a Number"))
    num2 = int(input("Enter a Number"))
    result = num1 / num2
except ValueError:
    print("InValid Input")
except ZeroDivisionError:
    print("Num2 is zero")
else:
    print(f"Result {result}")
finally:
    print("I will be always executed!!")

# num 1 - 10, pramod (ValueError)
# num 2 - 0

# ZeroDivisionError
# ValueError


# else and finally
