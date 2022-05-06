from math import sqrt


def checkprime(num):
    max = int(sqrt(num) + 1)
    prime = True
    
    for i in range(2,max):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True

    if num == 1:
        prime = False

    if prime == True:
        #print(str(num) + " is prime")
        return 1
    else:
        #print(str(num) + " is not prime")
        return 0

x = 1
primecount = 0
while x < 10000:    
    primecount += checkprime(x)
    x += 1

print(primecount) 