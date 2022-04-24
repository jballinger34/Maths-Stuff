from coscalc import cosine
from sincalc import sin

def tan(x,maxn):
    a = sin(x, maxn)
    b = cosine(x, maxn)
    t = a/b
    return t
