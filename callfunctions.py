from tancalc import tan
from sincalc import sin
from coscalc import cosine
from etothexcalc import etothex

x = 0
MAXN = 10

print("sin(" + str(x) + ") = " + str(sin(x,MAXN)))

print("cosine(" + str(x) + ") = "+ str(cosine(x,MAXN)))

print("tan(" + str(x) + ") = " + str(tan(x,MAXN)))

print("e^"+ str(x) +" = " + str(etothex(x,MAXN)))