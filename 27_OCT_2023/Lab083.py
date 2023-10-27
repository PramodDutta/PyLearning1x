# List is Mutable, Its content can be changed!
my_list = [1, 2, 3, 4, 5, 5]
print(my_list)
my_list[1] = 20
print(my_list)
print(type(my_list))

# Tuple - It is immutable in nature. - No modification
car = ("Ford GT", "Raptor", "Lambo", "Lambo")
car2 = ("Ford GT", True, "Lambo")
print(car)
print(type(car))
# car[1] = "XUV 500"

print(len(car))

# Tuple (), Its content can't be changed, List [] and it content can be changed!

# List can be converted

list1 = [1, 2, 3, 4, 5, 6]
print(tuple(list1))



