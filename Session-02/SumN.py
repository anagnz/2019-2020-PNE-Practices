# .. 1 +2 +3 + ...+ 20
# .. 1 + 2 +3 + ... + 100


def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


print("sum of 1-20 is: ", sumn(20))
print("sum of 1-100 is: ", sumn(100))
