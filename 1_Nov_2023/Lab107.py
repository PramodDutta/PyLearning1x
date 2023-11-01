numList = [30, 2, -15, 17, 9, 100]
list_of_numbers_grater_10 = list(filter(lambda sik: sik > 10, numList))
print(list_of_numbers_grater_10)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def is_even(num):
    return num % 2 == 0


even_numbers_tuple = tuple(filter(is_even, numbers_tuple))
print(even_numbers_tuple)

l = [(1, 23), (34, 34)]
print(l)
print(l[0])
print(l[0][0])
print(l[0][1])









