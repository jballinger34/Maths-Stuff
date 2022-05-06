from factorialcalc import factorial

def numerators(x,maxn):
    numeratorlist = []
    for n in range(0,maxn+1):
        tempnumerator = x**n
        numeratorlist.append(tempnumerator)
    return numeratorlist

def denominators(maxn):
    denominatorlist = []
    for n in range(0,maxn+1):
        tempdenominator = factorial(n)
        denominatorlist.append(tempdenominator)
    return denominatorlist

def etothex(x, maxn):
    num = numerators(x, maxn)
    denom = denominators(maxn)
    noverd = []
    runningsum = 0
    for a,b in zip(num,denom):
        noverd.append(a/b)
    for a in noverd:
        runningsum = a + runningsum
    ans = runningsum
    return ans 


if __name__ =="__main__":
    x = 1
    maxn = 10
    print(etothex(x,maxn))









# e^x = sum from n=0 -> n=infinity of:(x^n/(n)!)
