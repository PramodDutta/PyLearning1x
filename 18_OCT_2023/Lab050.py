scale = int(input("Enter the num\n"))
if scale >= 90 and scale <= 100:
    print("grade is A")
elif scale >= 80 and scale <= 89:
    print("grade is B")
elif scale >= 70 and scale <= 79:
    print("grade is C")
elif scale >= 60 and scale <= 69:
    print("grade is D")
elif scale >= 0 and scale <= 59:
    print("grade is F")
else:
    print("invalid input")

