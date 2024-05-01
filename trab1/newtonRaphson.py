from sympy import *
from math import *

def newtonRaphson(f, exp, x_zero, precisao):
    x = Symbol('x')
    # x**2 - 1 = exp
    f_prime = exp.diff(x)
    print(f_prime)
    f_prime = lambdify(x, f_prime)
    n = 0
    xk = x_zero

    if abs(f(x_zero)) < precisao:
        return x_zero
    
    while True:
        print(f"{n} - {xk} - {f(xk)}")
        xk = x_zero - (f(x_zero) / f_prime(x_zero))
        if abs(f(xk)) < precisao or abs(xk - x_zero) < precisao:
            n += 1
            print(f"{n} - {xk} - {f(xk)}")
            return xk
        x_zero = xk
        n += 1


