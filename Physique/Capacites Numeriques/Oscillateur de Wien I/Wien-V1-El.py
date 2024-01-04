# -*- coding: utf-8 -*-
"""
Created on 10/10/2021

@author:TRUONG Nell
"""

import numpy as np
from  scipy.integrate import odeint
import matplotlib.pyplot as plt 

R=1.0e3  #résistance du filtre de Wien en ohm.
C=10.0e-9  #condensateur du filtre de Wien en farad
w0= 1.0/ (R*C)   #pulsation propre du filtre

G=3.2#Gain de l’etage d’amplification

vsat=15 # tension de saturation de l’ALI en volt

#conditions initiales
e0= 0.01  # entree de l’etage d’amplitication ; 0.01 simule le bruit
de0= 0.01  # derivee de e ; 0.01 simule le bruit en entree
QC1  remplir CO   # vecteur Condition initiale

#Création de F(Y,t)
QC2  code de la fonction F(y,t) qui retourne [de ,dde] ,
 où dde est calculée à partir de  F1(Y,t) ou F2(Y(t) selon la condition 
sur e(t)


    
 #création du tableau de temps t
t0=0        #instant initial de la simulation en seconde
tfin=2e-3    #instant final de la simulation en seconde
dt=0.01e-3    #  pas de temps en seconde 
QC3  code permettant le calcul du nombre d’itération  n  
(qui doit un entier) à partir de la durée temporelle d’acquisition et du pas dt

QC4 code  créant le tableau de temps t  à l’aide de la commande linspace 

# Determination de l’entree de l’etage d’amplification      
QC5 code  permettant la résolution par odeint ,le tableau  retournéest nommé sol

QC6   code pour  récupérer les valeurs de e(t)  
QC7   code  récupérer les valeurs  de la dérivée temporelle de e(t)


#sortie de l'étage amplifiacteur
u = np.where(abs(e)>vsat/G,vsat*np.sign(e),e*G)

# Tracer des courbes
plt.subplot(3,1,1) # Figure du haut à gauche
 QC8  code permettant de tracer  u=f(t)
 QC9  code permettant de mettre le titre ‘Démarrage des oscillations’, 
 et  nommer  les axes (grandeurs+unités) 
plt.ylim(-16,16) # Pour bien voir l’ecretage

plt.subplot(3,1,2) # Figure du bas à gauche
 QC10  code permettant de tracer  e=f(t)
 QC11  code permettant de nommer  les axes (grandeurs+unités) 
 
plt.show()

