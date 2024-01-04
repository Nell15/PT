# -*- coding: utf-8 -*-
"""
Created on 

@author: -
"""
                # charge condensateur  script RCcharg-El.py à compléter
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constantes données par le sujet :

R = 1e3
C = 1e-6
E = 5.0
tau = R * C     # Temps de relaxation

CI = 0.0        # condition initiale
t0 = 0          # valeur  de départ
tf = 0.01       # valeur maximale  tf=10ms)
n = 100         # nombre d'itérations

## QC1  créer t avec linspace 
# création du tableau de temps t

t = np.linspace(t0, tf, n + 1)

#solution exacte
#QC2 écrire la fonction U(t)  permettant le calcul de la solution exacte u(t)

def U(t):
        return E * (1.0 - np.exp(-(t / tau)))

##QC3 écrire la commande permettant l’exécution de U(t) .

U = U(t)

#création de la fonction F(y,t) appelée ED(y,t)
##QC4 : écrire la fonction ED (y,t)  permettant de créer F(y,t)

def ED(y, t):
        return (E - y) / tau # retourne dy

#Résolution de l'équation différentielle par odeint
#QC5 : écrire la commande permettant la résolution par  odeint 

UOD = odeint(ED, CI, t)

#print(UOD)

#solution par Euler 
#QC6 : écrire la fonction Euler (ED,t)  permettant d’intégrer

def Euler(ED,t):
        tab = np.empty(n + 1)
        tab[0] = CI
        h = (tf - t0) / n
        for i in range(n):
                tab[i + 1] = tab[i] + h * ED(tab[i], t[i])
        return tab           

#par la méthode d’Euler.
#QC7 : écrire la commande permettant l’exécution de Euler (ED,t) .

UE = Euler(ED, t)
# print(UE)

#tracer des courbes
plt.clf() #efface la figure courante
#QC8  écrire la commande permettant de tracer  U=f(t) en trait plein rouge

plt.plot(t, U,'r')

#QC9  compléter la commande permettant de tracer UOD=f(t) avec des ‘+’
#sans ligne continue en bleu

plt.plot(t, UOD, 'b', marker = '+', linewidth = 0, label = 'odeint')

#QC10  compléter la commande permettant de tracer UE=f(t)  des  ‘o ‘ 
        #sans ligne continue en vert, et permettant d’afficher
        #la légende odeint correspondante .

plt.plot(t, UE, 'g', marker = 'o', linewidth = 0, label = 'Euler')
plt.ylabel("Tension aux bornes du condensateur")
plt.xlabel("Temps t")
plt.grid()
plt.legend(loc= 'right') #positionne la légende à droite
plt.show() #affiche les courbes 

# 13) 
commentaire = """Plus le nombre n de point est grand, plus les méthodes odeint et d'Euler se rapprochent de la 
de la solution exacte. Plus le nombre d'itération est grand, plus les points (+ et o) tendent à se superposer
avec la courbe donnée par la solution exacte mathématique."""
