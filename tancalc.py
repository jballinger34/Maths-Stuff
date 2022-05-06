from coscalc import cosine
from sincalc import sin



def tan(x,maxn):
    a = sin(x, maxn)
    b = cosine(x, maxn)
    t = a/b
    return t

if __name__ == "__main__":
    x= 3.14/2
    maxn = 10
    print(tan(x,maxn))
    