from factorialcalc import factorial

#n and r must be positive integers

n = 6
r = 0

def nCr(n,r):
    numerator = factorial(n)
    denominator = factorial(r)*factorial(n-r)
    return numerator/denominator

print(nCr(n,r))


