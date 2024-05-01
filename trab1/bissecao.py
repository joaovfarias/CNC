from math import *


def bissecao(a, b, f, n, precisao):
    if f(a) * f(b) > 0:
        print("Nao tem raiz")
        return

    x = (a + b) / 2
    if (abs(b - a)) < precisao or abs(f(x)) < precisao:
        return a
    
    M = f(a)
    for i in range(n):
        x = (a + b) / 2
        if (M * f(x)) > 0:
            a = x
        else:
            b = x
        if (abs(b - a)) < precisao or abs(f(x)) < precisao:
            return a
        
    return a