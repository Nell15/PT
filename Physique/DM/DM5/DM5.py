# -*- coding: utf-8 -*-
"""
Created on 02/10/2022

@author: TRUONG Nell
"""

import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants definition :

g = 9.81
z0 = 0              # initial height value, here 0 for ground level
zf = 11             # final height value, here is 11 km
n = 11000              # number of iteration
R = 8.314           # perfect gas constant

# For this examples, all values below were arbitrarily chosen.
M = 29
ALPHA = 4           # thermal gradient
T0 = 20 + 273.15    # Celcius converted to Kelvins
P0 = 101            # in kPa

# 1) Euler's scheme recurrence

z = np.linspace(z0, zf, n + 1)

def ED(P, z):
    return P * (- M * g) / (R * (T0 - ALPHA * z))

def Euler(ED, z):
    tab = np.empty(n + 1)
    tab[0] = P0
    h = (zf - z0) / n
    for i in range(n):
        tab[i + 1] = tab [i] + h * ED(tab[i], z[i])
    return tab

# Ploting the function :
PE = Euler(ED, z)
plt.clf()                                                           # clears any previous figure
plt.plot(z, PE, 'b', marker = 'o', linewidth = 0, label = 'Euler')  # draws the scatter plot
plt.grid()                                                          # creates a grid on the figure
plt.show()                                                          # shows the drawn plot

