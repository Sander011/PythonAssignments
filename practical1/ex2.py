import sys


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def frac(a, b):
    if b == 0 :
        return 'b cannot be zero'
    else :
        a, b = a / gcd(a, b), b / gcd(a, b)
        return str(a) + '/' + str(b)


print(gcd(1820, 231))

print(gcd(123456789, 987654321))
# so a 9 x 9 tile

frac(-3, 27)


