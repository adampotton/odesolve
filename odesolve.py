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
    A = 0
    md = method
    t1 = np.array(t); B = (t[-1] - t[0] ) / t[1] + 1   
    x1 = X0[0]
    el = []
    if md == euler:
        while A < B :
            x2 = solveto(f, x1, t1[A], t[-1], hmax, euler)
            A = A + 1
            el.insert(0, x2)         
        ar = np.array(el)
        xm = np.mat(ar)                 
        return xm
            
        
    if md == rk4:
        while A < B:
            x2 = solveto(f, x1, t1[A], t[-1], hmax, rk4)
            A = A + 1
            el.insert(0, x2)
        ar = np.array(el)
        xm = np.mat(ar)
        return xm
        
    pass
