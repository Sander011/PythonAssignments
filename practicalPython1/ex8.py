def divisors(a):
    result = []
    for i in range(a, 0, -1):
        # print(i)
        if a % i == 0:
            print(i)
            result.append(i)
    return result


def primeFactor(a):
    div = divisors(a)
    primes = []
    for i in div:
        if len(divisors(i)) == 2:
            primes.append(i)
    return primes
    # res = str(a) + ' = '

    # for j in primes:
    #     while a % j == 0:
    #         a = a / j
    #         res += str(j) + ' * '
    #
    #
    # res += str(i)
    # return res

def smartPrimeFactor(n):
    a = n
    b = 2
    c = 2
    primes = []
    while a != 1:
        if a % b == 0:
            a = a/b
            primes.append(b)
            c = b
        else:
            b+=1
    res = str(n) + ' = '

    for j in primes:
        while n % j == 0:
            n = n / j
            res += str(j) + ' * '

    res += str(1)
    return res


print(smartPrimeFactor(int(600851475143)))