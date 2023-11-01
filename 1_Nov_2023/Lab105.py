words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_len = 6


def check_len(w):
    return len(w) >= min_len


op = list(filter(check_len, words))
print(op)
