# user_input = input("Enter the inpout String\n")


# Palindrome
# Reverse the String and match with the old String it should be same.
# 1 By using a Traditional method
# 2 Built in functions

def reverse_string(input_string):
    reverse_str = ""
    for c in input_string:
        reverse_str = c + reverse_str
    return reverse_str


original_str = "NAMAN"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("It is not")