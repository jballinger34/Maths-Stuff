from factorialcalc import factorial

def coefficient(maxn):
    coefficientlist = []
    for n in range(0,maxn+1):
        tempcoefficient = (-1)**n
        coefficientlist.append(tempcoefficient)
    return coefficientlist

def numerators(x,maxn):
    numeratorlist = []
    for n in range(0,maxn+1):
        tempnumerator = x**(2*n)
        numeratorlist.append(tempnumerator)
    return numeratorlist

def denominators(maxn):
    denominatorlist = []
    for n in range(0,maxn+1):
        tempdenominator = factorial(2*n)
        denominatorlist.append(tempdenominator)
    return denominatorlist

def cosine(x, maxn):
    coeff = coefficient(maxn)
    num = numerators(x, maxn)
    denom = denominators(maxn)
    newnum = []
    fraction = []
    runningsum = 0
    for a,b in zip(coeff, num):
        newnum.append(a*b)
    for a,b in zip(newnum,denom):
        fraction.append(a/b)
    for i in fraction:
        runningsum = i + runningsum
    return runningsum
    
if __name__ == "__main__":
    x = 0
    maxn = 10
    print(cosine(x,maxn))