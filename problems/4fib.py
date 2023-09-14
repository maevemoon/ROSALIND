# 4 FIB Rabbits and Recurrence Relations

def Fibonacci(n, k):
    small = 1
    big =  1
    # update ages/amounts for every month
    for months in range(1, n-1):
        current = big + small*k
        small = big
        big = current
    return current

n = 32
k = 5
print(Fibonacci(n, k))
