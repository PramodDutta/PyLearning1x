# Fibonaci series
# 0,0+1, 0+1+1,
# n = 7


a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b
