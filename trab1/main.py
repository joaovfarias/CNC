from bissecao import bissecao
from falsapos import falsapos
from newtonRaphson import newtonRaphson
from secante import secante
from sympy import *
from math import *

f = lambda x : x**3 - x - 1

def main():
    x = Symbol('x')
    y = x**3 - x - 1
    secante(f, 0, 0.5, 10**-6)

if __name__ == "__main__":
    main()