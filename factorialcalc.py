def factorial(n):
    factorial = 1
    if n == 0:
        factorial = 1
    else:
        for i in range(1,n+1):
            factorial = factorial*i
    return factorial

if __name__ =="__main__":
    x = 5
    print(factorial(x))
