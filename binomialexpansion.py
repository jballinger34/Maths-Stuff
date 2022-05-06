from nCr import nCr



#function in terms of (aterm + xterm)^n
#when n is a positive integer, atermcoeff is a coeff to a y term
#when n isnt, atermcoeff is just a constant
#(3y+3x)^2
#or
#(3+3x)^-2
atermcoeff = 1
xtermcoeff = 1
n = 2
#for when n is not positive integer, maxterms defines the amount of terms in the binomial series are returned 
maxterms = 4

function = [atermcoeff,xtermcoeff,n]

def binomialexpansion(function,maxterms):
    if n == 0:
        return 1
    if abs(n) == n and type(n) == int:
        return basic(function)
    else:
        return general(function,maxterms)

def basic(function):
    a = function[0]
    x = function[1]
    n = function[2]
    terms = []
    for i in range(0,n+1):
        aterm = a**(n-i) 
        xterm = x**(i)
        term = str(nCr(n,i))+"*"
        if aterm == 0:
            pass
        elif (n-i) == 0:
            term += str(aterm) +"*"
        elif(n-i) == 1:
            term += "y*"
        else:
            term += str(aterm)+"y^"+str(n-i)+"*"
        if aterm == 0:
            pass
        elif (i) == 0:
            term += str(xterm)
        elif(i) == 1:
            term += "x*"
        else:
            term += str(xterm)+"x^"+str(i)
        terms.append(term)
    return terms


def general(function,maxterms):
    pass

print(binomialexpansion(function,maxterms))
