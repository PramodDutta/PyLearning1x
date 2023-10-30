my_dict = {'a': 1, 'b': 2}

val = my_dict.pop('a')
print(val)

print(my_dict)

# API Testing -> JSON so we can use Dict which is similar data type as JSON

print(dir(dict()))


# How to Iterate over the Dict?

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(len(knights))

for k,v in knights.items():
    print(k,v)


