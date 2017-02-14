from functools import reduce

from practical2.perm import *
p = [1,2,7,4,6,0,9,5,8,3]
# print(p)
# q = [2,3,7,6,1,0,9,5,8,4]
# print_permutation(p)
# print_permutation(q)
# print(p==q)
# r = trivial_permutation(10)
# print_permutation(r)

def composition(p, q) :
    res = []
    for i in range(len(p)):
        res.append(p[q[i]])
    return res

def inverse(p):
    temp = list(range(len(p)))
    for i in range(len(p)):
        temp[p[i]] = i
    print_permutation(temp)

def power(p, i) :
    res = p
    while i > 1:
        res = composition(res,p)
        i-=1
    print_permutation(res)

def period(p):
    res = p
    print_permutation(res)
    i = 1
    while not is_trivial(res):

        res = composition(res, p)
        print_permutation(res)
        i += 1
    print(i)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


def smart_period(p):
    c = cycles(p)
    res = 1
    while c:
        a = c.pop(0)
        res = lcm(len(a),res)
    print(res )


# p = test_permutation(1000)
smart_period(p)
