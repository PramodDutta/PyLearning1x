numbers = [1, -2, -3, -4, 5, 16, -7, 8, -9, -10]


def is_positive(num):
    return num > 0


pos_numbers = filter(is_positive, numbers)
print(pos_numbers)
pov_numbers_list = list(pos_numbers)
print(pov_numbers_list)
