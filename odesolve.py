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
    n = (t2 - t1) / hmax
    nfull = math.floor(n)
    hsmall = (t2 - t1) - (nfull * hmax)
    for i in range(nfull):
        x1 = euler(f, x1, t1, hmax)
    if 1 % n:
        return x1
    else:
        x1 = euler(f, x1, t1, hsmall)
        return x1
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    pass
