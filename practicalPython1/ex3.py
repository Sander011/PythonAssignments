import string

def encode(number):
    if number in range(0,10):
        return str(number)
    return string.ascii_uppercase[number-10]

def to_k(n, k) :
    res = ''
    while(n != 0):
        n, r = divmod(n, k)
        res = encode(r) + res
    return res

def decode(str):
    # convert to ASCII and apply conversion
    if(ord(str) < 58) :
        return ord(str) - 48
    return ord(str) - 55

def from_k(s, k) :
    res = 0
    power = len(s) - 1
    for c in s:
        res += decode(c) * pow(k, power)
        power -= 1
    return res

def convert(k, m, s):
    return to_k(from_k(s, k), m)

tryout = []
for i in range(36) :
    tryout.append(encode(i))
for j in tryout :
    print(j)
    print(decode(j))

print(from_k('10E1', 16))
print(convert(2, 4, '10011010'))