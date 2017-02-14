def findMiddle(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                return b
            else:
                return c
        else:
            return a
    else:
        if b > c:
            if c > a:
                return c
            else:
                return a
        else:
            return b

def minmaxlist(list):
    curMin = list[0]
    curMax = list[0]

    for i,j in zip(*[iter(list)]*2):
        if i < j:
            if i < curMin:
                curMin = i
            if j > curMax:
                curMax = j
        else:
            if i > curMax:
                curMax = i
            if j < curMin:
                curMin = j

    return 'Max = ' + str(curMax) + ', Min = ' + str(curMin)

def testfunctions():
    print(findMiddle(18, 2, 7))
    print(findMiddle(2, 7, 18))
    print(findMiddle(2, 18, 7))
    print(findMiddle(18, 7, 2))
    print(findMiddle(7, 2, 18))
    print(findMiddle(7, 18, 2))

    print(minmaxlist([-5,10,-3, 17]))


testfunctions()