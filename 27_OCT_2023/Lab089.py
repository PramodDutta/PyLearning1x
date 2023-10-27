t=("TheTestingAcademy","for","TheTestingAcademy")
print("\nSet with the use of Tuple: ")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.difference(set2)
my_set2 = set2.difference(set1)
print(my_set)
print(my_set2)


set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]
# l3 = l1



set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)

for i in set1:
	print(i)

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])


set1.remove(5)
set1.remove(6)
print(set1)





