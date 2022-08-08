# odesolve.py
#
# Author: <insert name>
# Date:   <insert date>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

import numpy as np
import math

def euler(f, x, t, h):
    return x + h * f(x, t)
    pass


def rk4(f, x, t, h):
    def f(x, t):
        return x
    k1 = f(x, t)
    k2 = f(x + k1 * h * 0.5, t + h * 0.5)
    k3 = f(x + k2 * h * 0.5, t + h * 0.5)
    k4 = f(x + k3 * h, t + h)
    xn1 = x + (k1 + 2 * k2 + 2 * k3 + k4) * (h / 6)
    return xn1
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):
    md = method
    if md == euler:
        while t1 <= t2:
            xn = x1
            x1 = euler(f, x1, t1, hmax)
            t1 = t1 + hmax
            if t1 == t2:
                return x1
            elif t1 > t2:
                hmin = t2 - t1 + hmax
                t1 = t1 - hmax
                return euler(f, xn, t1, hmin)
    elif md == rk4:
        while t1 <= t2:
            xn = x1
            x1 = rk4(f, x1, t1, hmax)
            t1 = t1 + hmax
            if t1 == t2:
                return x1
            elif t1 > t2:
                hmin = t2 - t1 + hmax
                t1 = t1 - hmax
                return rk4(f, xn, t1, hmin)
    pass
    


def odesolve(f, X0, t, hmax, method=euler):
    if isinstance(X0, np.ndarray):
        el = []
        for A in t:
            el.append(solveto(f, X0, 0, A, hmax, method))
        return np.array(el)
    el = []
    for B in X0:
        el2 = []
        for C in t:
            result_x.append(solveto(f, B, 0, C, hmax, method))
        result.append(el2)
    return np.array(el)
        
        
    pass
