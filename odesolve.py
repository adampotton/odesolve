# odesolve.py
#
# Author: <insert name>
# Date:   <insert date>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

import numpy as np

f = 0

def euler(f, x, t, h):
    def f(x, t):
        return x + t
    return x + h * f(x, t)
    pass


def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    pass
