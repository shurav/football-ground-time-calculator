import math
import cmath
def quadratic(a, b, c):
    discrim = (b**2-4*a*c)
    if(discrim < 0):
        discrim = -1*discrim
        realValue = math.sqrt(discrim)
        result = complex(0, realValue)
        x1 = (((-b+result)/(2*a)))
        x2 = (((-b-result)/(2*a)))
    else:
        x1 = (((-b+math.sqrt(discrim))/(2*a)))
        x2 = (((-b-math.sqrt(discrim))/(2*a)))
    return (x1, x2)
