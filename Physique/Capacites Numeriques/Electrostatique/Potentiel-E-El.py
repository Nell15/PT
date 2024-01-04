#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
       Tracer des équipotentielles et lignes de champ pour 
       une distribution de charges 
                     Potentiel-E-El.py
'''

import numpy as np
import matplotlib.pyplot as plt



'''
         #### Calcul du potentiel et  Tracer des équipotentielles #### 
'''


#distribution de charges
e=1.6e-19
distrib=[[e,50,25],[-e,50,75] ]


#coordonnées des charges de la distribution     
# QC1 compléter le code 
def position_charges(distrib):
    coor_charges=[]
    for charge  in distrib:
        i, j = charge[1], charge[2]
        coor_charges.append([i, j])
    return coor_charges


#distance ri entre le point 𝑀 et une charge 𝑞𝑖 
#  QC2  fonction distance(charge,i,j) qui retourne ri en µm

def distance(charge, i, j):
    icharge, jcharge = charge[1], charge[2]
    d = np.sqrt((icharge - i) ** 2 + (jcharge - j) ** 2)
    ri = d * 10e-6
    return ri

# potentiel électrostatique créé par la charge [i,j].
# QC3  compléter le code 
def potentiel(charge,i,j):
    eps0=8.85e-12   
    qi = charge[0]
    ri = distance(charge, i, j)
    V = qi / (4 * np.pi * eps0 * ri)
    return V

# initialise le tableau V
N = 100
#  QC4 initialiser V 
V = np.zeros((N, N))


#  potentiel en tout point du Domaine 
# QC5 compléter le code 
 
def calcul_potentiel(distrib, V):
    positionsCharges = position_charges(distrib)
    N = 100
    for i in range(N):
        for j in range(N):
            if [i,j] not in positionsCharges: # on se place en dehors des points occupés par les charges
                Vij = 0
                for charge in distrib :
                    Vij = potentiel(charge, i, j) # calculer Vij 
                V[i,j] = Vij
    return V

V = calcul_potentiel(distrib,V)

#Tracer équipotentielles 


plt.clf()
plt.imshow(V)
'''
QC6 tracer des équipotentielles avec  plt.contour
'''
plt.contour(V, 200, cmap = 'Oranges')
plt.show()

'''
      ######    Calcul du champ électrique à partir du potentiel #####
'''

# QC7 
#E  créé par le potentiel  [i,j].
a = 1 * 10e-6
def champE(V,i,j):
    Ex = - (V[i, j + 1] - V[i, j]) / a
    Ey = - (V[i + 1, j] - V[i, j]) / a
    return Ex, Ey


#  E en tout point du Domaine 
def calcul_champE(V,distrib):
    # QC8 compléter le code 
    N=100
    Ex=  # initialiser le tableau NxN 
    Ey= # initialiser le tableau NxN 
    positions_charges=position_charges(distrib)
    
    for i in range ?? :
        for j in range ??:
            if ([i,j] ???) and ([i,j+1] ????) and ([i+1,j]???):
                ????????
    return Ex,Ey


Ex,Ey=calcul_champE(V,distrib)

#TRacer des équipotentielles et lignes de champ
plt.rcParams['figure.figsize']=[9,9]
plt.clf()
plt.imshow(V)

#  QC6 tracer des équipotentielles avec  plt.contour
#  QC9 rtacer des lignes de champ avec plt.streamplot
 
plt.show()