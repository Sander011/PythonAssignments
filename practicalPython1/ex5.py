def largePalindrome():
    max = 0
    for i in range(999 , 100, -1):
        for j in range(999, i, -1) :
            num = i * j
            if(str(num) == str(num)[::-1] and num > max) :
                max = num

    return max

print(largePalindrome())