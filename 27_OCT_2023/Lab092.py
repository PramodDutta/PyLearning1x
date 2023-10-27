list1 = [10, 20, 30, 40]
tuple1 = (10, 20, 30, 40)
print(list1)


def mul_by10(a):
    a[0] *=10
    a[1] *=10
    a[2] *=10
    a[3] *=10


print(list1)
mul_by10(list1)
mul_by10(tuple1)
print(list1)
print(tuple1)