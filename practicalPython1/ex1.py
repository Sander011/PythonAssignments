def multiples(n1, n2):
    result = 0
    i = 0
    count = 1000
    while i < count :
        if(i % n1 == 0 or i % n2 == 0):
            result = result + i
        i = i + 1
    return result

print(multiples(3, 5))