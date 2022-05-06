#needs work


def coefficient(maxn):
    coefficientlist = []
    for n in range(1,maxn+1):
        tempcoefficient = (-1)**(n+1)
        coefficientlist.append(tempcoefficient)
    return coefficientlist

def numerators(x, maxn):
    numeratorlist = []
    for n in range(1,maxn+1):
        tempnumerator = x**n
        numeratorlist.append(tempnumerator)
    return numeratorlist

def denominators(maxn):
    denominatorlist = []
    for n in range(1,maxn+1):
        tempdenominator = n
        denominatorlist.append(tempdenominator)
    return denominatorlist

def ln(x,maxn):
    coeff = coefficient(maxn)
    num = numerators(x,maxn)
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

if __name__=="__main__":
    x = 2
    maxn = 10
    print(ln(x,maxn))
'''

ln(1+x) = sum from n=1 -> n= infinity of: ((-1)^n+1)(x^n)/n


'''