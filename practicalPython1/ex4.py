def fibCount(n):
    res = 0
    a = 0
    b = 1
    while b < n:
        a, b = b, a + b
        if b % 2 == 0:
            res += b
    return res

print(fibCount(4000000))