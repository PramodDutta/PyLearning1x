# Map and Filter in the List


# Map Functions ( where we will go from one item and apply a functions)
numbers = [1, 2, 3, 4, 5]
# sq_numbers = [1, 4, 9, 16, 25]
sq = lambda x: x * x
sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)


def ThreeTimes(a):
    return a ** 3


# Map Function
sq_numbers3 = list(map(lambda x: x * 3, numbers))
sq_numbers2 = list(map(ThreeTimes, numbers))
print(sq_numbers2)
print(sq_numbers3)
