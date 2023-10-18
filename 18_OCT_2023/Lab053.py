# Break and Continue with the Loops

# Break
# 1 to 10 -> break when value of count = 5 -> 1,2,3,4,5,x
# put the debug point when you see condition
# count = 1
# while count <= 10:
#     print(count)
#     if count >= 5:
#         break
#     count = count + 1

# I want to break when count = 5

for counter in range(1, 10):
    if counter == 5:
        break
    print(counter)
print("For loop is finished")
