side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Eq")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Iso")
else:
    print("Scalene")

