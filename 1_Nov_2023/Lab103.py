numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# num%2==0
# even_numbers = [2, 4, 6, 8, 10]


# filter -> Number element can be less or equal the list

def is_even(num):
    return num % 2 == 0


# Mod
# 2| 10 | 5
#    10
#    ---
#    0

even_numbers = filter(is_even, numbers)
print(even_numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)