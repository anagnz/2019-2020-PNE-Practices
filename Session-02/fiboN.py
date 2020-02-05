def fibo(n):
    index1 = 0
    index2 = 1
    sumn = 0
    for number in range(0, n+1):
        if number == 0:
            sumn = 0
        elif number == 1:
            sumn = 1
        else:
            sumn = index1 + index2
            index1 = index2
            index2 = sumn
    return sumn


print("5th Fibonacci termn: ", fibo(5))
print("10th Fibonacci term: ", fibo(10))
print("15th Fibonacci term: ", fibo(15))
