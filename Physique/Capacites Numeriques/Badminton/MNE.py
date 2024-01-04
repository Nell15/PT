# -*- coding: utf-8 -*-
# Created on Fri Dec 23 07:05:00 2022
# @author: mhebding

# 0.
# IMPORT ET VARIABLES GLOBALES

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m : float = 5.3 # en g
g : float = 9.81 # en m.s^-2
Te : float = 45 * 10**-3 # en s

## PREPARATION

# 1.
pointage = np.loadtxt("pointage.txt",skiprows=1) # A COMMENTER
Xexp = pointage[:,5] # A COMMENTER
Yexp = pointage[:,6] # A COMMENTER
# plt.figure('Donnees experimentales')
# plt.plot(Xexp,Yexp, 'o', label='Donnees brutes')
# plt.legend()
x = Xexp - Xexp [0] # A COMMENTER
y = -(Yexp - Yexp[0]) # A COMMENTER

# print(Xexp)
# print(Yexp)
r1 = """
La 1ere ligne récupère le contenu du fichier
Les deux et 3e lignes font des antépénultièmes et 
pénultièmes colonnes colonnes des listes
Les deux dernières lignes suppriment les premières valeurs 
des listes qui correspondent aux titres des colonnes dans le txt."""


# 2.
def exp():
    plt.figure('Donnees experimentales')
    plt.plot(x,y, 'o', label='Donnees brutes')
    plt.legend()
    plt.show()

# exp()

## MODELISATION

"""
# RESULTATS THEORIQUES ICI
"""

# 3.
# Modèle linéaire :
Vxlim : float = (x[-1] - x[-2]) / Te
Vylim : float = (y[-1] - y[-2]) / Te
Vlim : float = np.sqrt((Vxlim ** 2) + (Vylim ** 2))
# print('Vlim= '+str(round(Vlim,3))) # valeur de l'auteur 6.7 m/s

a = m * g / Vlim
b = m * g / (Vlim ** 2)
# 4.
# A COMPLETER
Vx0 : float = (x[1] - x[0]) / Te
Vy0 : float = (y[1] - y[0]) / Te
V0 : float = np.sqrt((Vx0 ** 2) + (Vy0 ** 2))
# print('V0= '+str(round(V0,3))) # valeur de l'auteur 40 m/s

# 5.
def A_lin(Vx, Vy):
    Ax = (-a / m) * Vx
    Ay = (-a / m) * Vy - g
    return Ax, Ay

def A_quad(Vx, Vy):
    V = np.sqrt(Vx * Vx + Vy * Vy)
    Ax = (-b / m) * V * Vx
    Ay = (-b / m) * V * Vy - g
    return Ax, Ay
# 6.
dt : float = Te / 50 # pas
N  : int = int((Te / dt) * len(x)) # nombre de points

def euler_V(acceleration):
    t = 0 # initialisations
    Vx = Vx0
    Vy = Vy0
    liste_t = [t]
    liste_Vx = [Vx]
    liste_Vy = [Vy]
    for n in range(N):
        t += dt
        Ax, Ay = acceleration(Vx, Vy)
        Vx += Ax * dt
        Vy += Ay * dt
        liste_Vx.append(Vx)
        liste_Vy.append(Vy)
        liste_t.append(t)
    return liste_t, liste_Vx, liste_Vy
# ????????
# Pas compris, valeurs, tableaux?
# print(euler_V(A_quad))

# 7.
def euler_OM(Vx,Vy):
    x = 0
    y = 0
    t = 0
    liste_X = [x]
    liste_Y = [y]
    for n in range(len(Vx)):
        # liste_X.append(liste_X[-1] + dt * Vx[t])
        # liste_Y.append(liste_Y[-1] + dt * Vy[t])
        x += Vx[n] * dt
        y += Vy[n] * dt
        liste_X.append(x)
        liste_Y.append(y)
    return liste_X, liste_Y
    # for n in range(len(Vx)):
    #     x += Vx[n] * dt
    #     y += Vy[n] * dt
    #     liste_X.append(x)
    #     liste_Y.append(y)
    # return liste_X, liste_Y

# 8.
# A ECRIRE POUR CALCULER t, Vx_lin, Vy_lin
# A ECRIERE POUR CALCULER X_lin, Y_lin
t, Vx_lin, Vy_lin = euler_V(A_lin)
X_lin, Y_lin = euler_OM(Vx_lin, Vy_lin)
# A ECRIRE POUR CALCULER t, Vx_quad, Vy_quad
# A ECRIRE POUR CALCULER X_quad, Y_quad
t, Vx_quad, Vy_quad = euler_V(A_quad)
X_quad, Y_quad = euler_OM(Vx_quad, Vy_quad)

def comparaison():
# A ECRIRE POUR AFFICHER LA TRAJECTOIRE EXPERIMENTALE ET LES DEUX MODELES
    plt.legend()
    plt.plot(X_lin, Y_lin, label="Modèle linéaire")
    plt.plot(X_quad, Y_quad, label="Modèle quadratique")
    plt.plot(x,y, '.', label='Trajectoire du volant')
    plt.show()
comparaison()

# 9.
def auteur():
# A COMPLETER
    V0 : int = 40 # en m/s
    alpha : float = 52 * np.pi / 180
    Vx0 : float = np.cos(alpha) * V0
    Vy0 : float = np.sin(alpha) * V0
    Vlim : float = 6.7 # en m/s
    t, Vx_lin, Vy_lin = euler_V(A_lin)
    AX_lin, AY_lin = euler_OM(Vx_lin, Vy_lin)
    t, Vx_quad, Vy_quad = euler_V(A_quad)
    AX_quad, AY_quad = euler_OM(Vx_quad, Vy_quad)

    plt.plot(X_lin, Y_lin)
    plt.plot(AX_lin, AY_lin, 'r')
    plt.plot(X_quad, Y_quad)
    plt.plot(AX_quad, AY_quad, 'r')
    plt.show()
    
auteur()

commentaire : str = """Les courbes étant superposée, les indications de l'auteur 
sont pertinentes"""

# 10.
"""
Cinem est un tableau numpy (= une liste de listes) qui contient les vecteurs cinematiques du volant a l instant t.
Cinem[0] = liste des x(t)
Cinem[1] = liste des y(t)
Cinem[2] = liste des Vx(t)
Cinem[3] = liste des Vy(t)

DerivC est une fonction qui, connaissant Cinem a l instant t renvoie sa derivee (idem methode d Euler).
"""

def DerivC(Cinem,t): # prends X, Y, Vx, Vy
    Ax, Ay = A_quad(Cinem[2],Cinem[3])
    return [Cinem[2],Cinem[3], Ax, Ay] # retourne Vx, Vy, Ax, Ay

t = np.linspace(0,Te*len(x),N)
Cinem = odeint(DerivC,[0,0,Vx0,Vy0],t)
X_odeint = Cinem[:,0]
Y_odeint = Cinem[:,1]

def exp_euler_odeint():
# INSTRUCTIONS GRAPHES EXP, EULER VS ODEINT
    pass

#exp_euler_odeint()