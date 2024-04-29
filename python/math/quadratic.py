# The quadratic equation :)

def quadratic_solver(a, b, c):
    d = (b**2) - (4*a*c)
    if (d < 0): print('There is no solution to this problem')
    else:
        x1 = (-b + (d**1/2)) / 2*a
        x2 = (-b - (d**1/2)) / 2*a
        print('The roots of the equation are ' + str(x1) + ' and ' + str(x2))
    
quadratic_solver(-4.9 * (10**-8), 2.7 * (10**-4), 1)