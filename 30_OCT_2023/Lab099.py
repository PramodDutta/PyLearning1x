

my_dict = {'b': 2, 'a': 1, 'c': 3}
print(my_dict)
val = my_dict.pop('a')
print(val)
# print(my_dict.pop('b'))
# print(my_dict.pop('c'))
print(my_dict)
my_dict['a'] = val
print(my_dict)


# OrderedDict
# key-value pairs based on the order of insertion

# list, set, tuple, dict, OrderedDict, - API Automation and Selenium

from collections import OrderedDict
od =  OrderedDict()
od['a'] = 45
od['c'] = 78
od['b'] = 97
od['d'] = 31

print(od)

# Selenium - Insert the Web elements into a Dict
# You want to keep the order - login elemtns, dashboard elements,

# Dict - It will not keep the Order of insertion
# OrderedDict - It will keep the order of insertion

keys = list(od.keys())
print(keys)
keys_sort=sorted(keys)
print(keys_sort)

keys_sort_rev=sorted(keys, reverse=True)
print(keys_sort_rev)



od2 = OrderedDict()
od2[keys_sort[0]] = 45
od2[keys_sort[1]] = 78
od2[keys_sort[2]] = 89
od2[keys_sort[2]] = 109
print(od2)

