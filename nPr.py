from factorialcalc import factorial

n = 10
r = 10

def nPr(n,r):
    numerator = factorial(n)
    denominator = factorial(n-r)
    return numerator/denominator

print(nPr(n,r))