tuple3 = tuple(["Pramod", "Lucky"])
print(tuple3)
print(tuple3[0])
print(tuple3[1])

# Merging Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

# Convert to List
my_tuple = (1, 2, 3, 4, 5)
print(list(my_tuple))

x = 10
a, b = 23, 34  # This is multiple value assign
q, w, e = (45, 56, 78)  # tuple assigned to multiple variables
print(q)
print(w)
print(e)


# Nested Tuples

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)
print(len(awesome_team))
print(awesome_team[0])
print(awesome_team[1])


print(awesome_team[0][1]) # Bruce
print(awesome_team[1][1]) # Diana Prince


# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("Moscow" in cities)

