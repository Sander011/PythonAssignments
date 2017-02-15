def fact(n, k):
    res = 1
    while n > k :
        res *= n
        n -= 1
    return res

def binom(n, k):
    return fact(n,n-k)/fact(k,0)

print(fact(28, 0))
print(binom(12,8))