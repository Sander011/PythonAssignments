def divisors(a):
    result = []
    for i in range(a, 0, -1):
        if a % i == 0:
            result.append(i)
    return result


def primeFactor(a):
    div = divisors(a)
    primes = []
    for i in div:
        if len(divisors(i)) == 2:
            primes.append(i)
    res = str(a) + ' = '

    for j in primes:
        while a % j == 0:
            a = a / j
            res += str(j) + ' * '


    res += str(i)
    return res

print(divisors(100))
print(primeFactor(100))
