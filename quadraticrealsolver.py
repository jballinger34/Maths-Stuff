
# define a quadritic ax^2 + bx + c = 0
# input a,b,c below

a = -1
b = 0
c = 1

def SolveQuadratic(a,b,c):
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print("There Are No Real Solutions")
    elif discriminant == 0:
        sol = (-b)/(2*a)
        print("There is One Real Solution: " + str(sol))
    else:
        sol1 = (-b + discriminant**0.5)/(2*a)
        sol2 = (-b - discriminant**0.5)/(2*a) 
        print("There Are Two Real Solutions: " + str(sol1) + " And " + str(sol2))

SolveQuadratic(a,b,c)
        
    


