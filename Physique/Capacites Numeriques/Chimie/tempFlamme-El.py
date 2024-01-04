#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

## Description du milieu réactionnel
C0 =150# concentration initiale en réactifs en mol/m^3
V = 1*1e-2 # volume du réacteur isochore en m^3

"""
      ###  partie cinétique ###
"""


### Données cinétiques
k =  0.000995# constante de vitesse

QC1 ###tableau de temps t  
N = 1000
tmax= ???
t= ???



### Fonction à résoudre avec odeint
def Chi(C,t):
   QC2 

C =QC3


plt.figure(1)
QC4
plt.xlabel('t en s')
plt.ylabel(r'C en mol.L$^{-1}$')
plt.grid(True)
plt.show()

""""
            ##   partie thermodynamique ##
"""
# Données thermodynamiques

T0 = 300 # température initial en kelvin
DrH0 = -94600 # enthalpie standard de réaction en J/mol
ceau = 4185 # capacité thermique massique du solvant en J/kg/K
rho = 1000 # masse volumique du solvant en kg/L


### Calcul de la température du milieu réactionnel
QC5

plt.figure(2)
QC6 
plt.xlabel('t en s')
plt.ylabel('Température en K')
plt.grid(True)
plt.show()

