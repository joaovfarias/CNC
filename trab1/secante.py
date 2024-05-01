from math import *

def secante(f, x_zero, x_um, precisao):
    if abs(f(x_zero)) < precisao:
        return x_zero
    if abs(f(x_um)) < precisao:
        return x_um
    
    n = 2
    
    while True:
        xk = x_um - ((f(x_um) * (x_um - x_zero)) / (f(x_um) - f(x_zero)))
        print(f"{n} - {xk} - {f(xk)}")
        if abs(f(xk)) < precisao:
            return xk
        x_zero = x_um
        x_um = xk
        n += 1
