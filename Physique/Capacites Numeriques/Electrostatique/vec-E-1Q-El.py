#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:11:12 2021

@author: maria
"""
"""
(1)Champ électrostatique créé par une charge ponctuelle à l'origine
                            vec-E-1Q-El.py
"""

import numpy as np
import matplotlib.pyplot as plt

#Paramètres du maillage
xmin = -2.1
xmax = 2.1
ymin =-2.1
ymax = 2.1

#choix du pas pour le maillage de l'espace : 
h = 0.33 
#abcisses et ordonnées 
# QC1 et QC2 X et Y avec np.arange
X = np.arange(xmin, xmax, h)
Y = np.arange(ymin, ymax, h)

# noeuds du maillage .

# QC3 XX et YY  avec np.meshgrid
XX, YY = np.meshgrid(X, Y)

#Coordonnées de position et charge de la charge ponctuelle
# QC4 X1,Y1=  ???   positionner à l origine  #Coordonnées de position de la charge 
K= 9.0e9  # valeur de la constante électrostatique 1/(4 pi epsilon0)
e=1.6e-19  #charge élémentaire

X1, Y1 = 0, 0

# QC5 valeur de Q1    # valeur de la charge 
Q1 = (-e) / K

#Distance de la charge 
# QC6 : distance R1 entre (X1,Y1) et (XX,YY) 
R1 = np.sqrt((XX - X1) ** 2 + (YY - X1) ** 2)

#Calcul de Ex et Ey 
# Ex = Q1*(XX-X1)/(R1**2)  
# Ey = Q1*(YY-Y1)/(R1**2)
Ex1 = Q1*(XX-X1)/(R1**2)  
Ey1 = Q1*(YY-Y1)/(R1**2)

# avec une 2e charge
X2, Y2 = -1.1, 0
Q2 = (e) / K
R2 = np.sqrt((XX - X2) ** 2 + (YY - X2) ** 2)
Ex2= Q2*(XX-X2)/(R2**2)  
Ey2 = Q2*(YY-Y2)/(R2**2)

Ex = Ex1 + Ex2
Ey = Ey1 + Ey2

# Que fait plt.quiver?
# trace le champs de vecteurs (U, V) avec les flèches aux points de coordonées (X, Y), en rouge

#normalisation de E  

#QC7   calcul de la norme de E notée EN  
EN = np.sqrt(Ex ** 2 + Ey ** 2)
ExN=Ex/EN
yN=Ey/EN


#Dessin graphique
plt.figure()
# QC8  plot de la charge (O bleu) 
plt.plot(X1,Y1,Ex,Ey,'o',color='blue')
plt.plot(X2,Y2,Ex,Ey,'o',color='blue')

# plt.quiver(XX,YY,Ex,Ey,color='red') #Champ vectoriel de tracé

plt.quiver(XX,YY,ExN,yN,color='red') #Champ vectoriel de tracé

plt.xlim([xmin,xmax]) #Plage de X à dessiner
plt.ylim([ymin,ymax]) #Plage de y pour dessiner
plt.grid()
plt.show()