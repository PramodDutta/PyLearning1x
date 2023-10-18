# Compare two numbers:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


result = "greater than" if num1 > num2 else "less than" if num1 < num2 else "equal to"
print(f"{num1} is {result} {num2}")