#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

A, B = 11095, 23.9
n1, n2 = 1.0, 3.0  #nbre de moles initiaux 
T = 400   #température
P = 1   #pression en bar
P0 = 1 #pression standard = 1bar

# QC1
def K(T):
    return np.exp((A / T) - B)

# QC2
def f(x):
    N = 4 * (x ** 2) * ((n1 + n2 - 2 * x) ** 2) * (P0 ** 2)
    D = (n1 - x) * ((n2 - 3 * x) ** 3) * (P ** 2)
    return (N / D) -  K(T) # on retourne Qr_eq = N / D

    
# QC3
def dichotomie (f, a, b, precision = 10**-5): 
    assert f(a)* f(b ) <= 0, " pas de solution dans [a , b] ! "
    # Inversion des bornes pour avoir a < b
    if a > b : a, b = b, a
    # Cas triviaux
    if f(a) == 0 : return a
    elif f(b) == 0 : return b
    # Recherche par dichotomie
    while abs(b - a) > precision:
        m = (a + b) / 2
        if f(a) * f( m) < 0:
            b = m
        else:
            a = m 
    return m
    
#valeurs des paramètres 
A, B = 11095, 23.9
n1, n2 = 1.0, 3.0  #nbre de moles initiaux 
T = 400   #température
P = 1   #pression en bar

#QC4 caclcul avec bisect
a, b = 0, 0.999
ksi = opt.bisect(f, a, b)
#Qc5 calcul avec dichotomie 
ksi2 = dichotomie(f, a, b)

# Note il semble y avoir

print("L'avancement à l'équilibre avec bisect est ksi = ", ksi)
print("L'avancement à l'équilibre avec dichotomie est ksi = ", ksi2)

"""

"""

####   influence de la température à P=1bar ####



# QC6 création de la liste Temp
Temp = list(range(300, 801, 1))

# QC7 créer Rt avec bisect
Rt = []
for T in Temp :
    Rt.append(opt.bisect(f, a, b))

# QC8
# plt.figure(1)
# plt.plot(Temp, Rt, color = 'dodgerblue')
# plt.title("Evolution du rendement avec la température ")
# plt.xlabel("T en K")
# plt.ylabel("Rendement")
# plt.show()

####   influence la pression sur le rendement à T = 400 K ####

T = 400
# QC9 création de la liste Pre
Pre = list(range(1, 51, 1))
Rp = []
#QC10 créer Rp avec bisect
for P in Pre :
    Rp.append(opt.bisect(f, a, b))
    
# QC11 
# plt.figure (2)
# plt.plot(Pre, Rp, color = 'r')
# plt.title("Evolution du rendement avec la pression")
# plt.xlabel("P en bar")
# plt.ylabel("Rendement")
# plt.show()


###   influence de la composition initiale à T = 400 K sous P = 1 bar ####

T = 400
P = 1
n1 = 1.0

# QC12 création de la liste N
N = []
for i in range(1, 251):
    N.append(i / 10)

Rn = []
X = [] # liste des valeurs de la fraction molaire en ammoniac

# QC13  création de Rn et X 
for n2 in N:
    M = min(0.999,n2/3.001)
    x = opt.bisect(f, 0, M)
    Rn.append(x)
    X.append((2 * x) / (n1 + n2 - 2 * x))
     
plt.figure(3)

# QC14
plt.plot(N, Rn, color = 'g')
plt.title("Evolution de l'avancement à l'équilibre" )
plt.xlabel(" n2 en mol" )
plt.ylabel(" Avancement à l'équlibre ( en mol )" )
plt.show()

plt.figure (4)
# QC15
plt.plot(N, X, color = 'orange')
plt.title (" Evolution de la fraction molaire en ammoniac ")
plt.xlabel ( " n2 en mol " )
plt.ylabel ( "Fraction molaire en ammoniac à l'équilibre " )
plt.show()