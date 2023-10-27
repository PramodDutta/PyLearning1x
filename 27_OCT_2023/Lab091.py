num = 20

def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n


op = multiply_by_10(num)
print(op)
print("Value of num outside function:", num)
