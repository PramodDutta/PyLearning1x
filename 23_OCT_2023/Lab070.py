original_str = "Pramod"
reverse_str = lambda original_str : original_str[::-1]


if reverse_str("Pramod") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")



add = lambda x,y : x+y

print(add(3,4))