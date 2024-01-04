# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

t = 60 * np.array([0,5,10,20,30,35]) # conversion en s
C = np.array([73e-3, 53e-3, 42e-3, 24e-3, 12e-3, 9e-3])

   # incertitude sur C (6%)
C_u = (5/100)*C

####   Méthode différentielle ####

V = []
# QC1  création de la liste de vitesse instantané
for i in range(len(t) - 1):
  Vi= -(C[i + 1] - C[i]) / (t[i + 1] - t[i])
  V.append(Vi)

lnV = np.log(V)

# QC2
lnA = []
for i in range(len(C) - 1):
  lnA.append(np.log(C[i]))

# Tracé de la courbe lnv en fonction de lnA ; régression linéaire
plt.figure(1)
# QC3 
plt.plot(lnA, lnV, 'bo')
#   insérer en deuxième temps  QC4 et QC5
p = np.polyfit(lnA, lnV, 1)


plt.xlabel( "ln(A) ")                             
plt.ylabel( "ln(V) ")                            
plt.title("Méthode différentielle")                  
plt.grid()
plt.show()


# QC6 : Affiche la pente  de la droite

"""

"""
         ####   Méthode intégrale ####
"""


lnC = np.log(C)

u_ln_C = C_u/C    # incertitude sur lnC (loi de composition des incertitudes)

p1=???   QC7 régression linéaire

# Tracé avec les barres d'erreur 

plt.figure(2)
plt.errorbar(t, lnC, yerr=2*u_ln_C  , fmt='o')  
plt.plot(t,lnC,'o') 

QC8 tracer de la droite de régression linéaire 

plt.grid(True)
plt.xlabel( " t en s")
plt.ylabel("ln(C)")
plt.show()  

 #print('ordre de la réaction k =',-p1[0], 's-1')  


"""
         ####  Calculs des résidus ####
"""
 
res=  QC11  
En = res/u_ln_C # résidus normalisés


plt.figure(3)
plt.errorbar(t, res, yerr =2* u_ln_C, fmt = 'o') # résidus avec barres d'incertitude-type
plt.plot([np.min(t), np.max(t)], [0, 0], '--') # pour mieux visualiser la droite correspondant à un résidu nul
plt.plot(t,res ,'o') 
plt.xlabel(" t en s")
plt.ylabel("résidus")
plt.grid()

plt.figure()
plt.plot(t, En, 'bo')        # écarts normalisés
 #tracé des deux traits horizonatux correspondant aux limites acceptables pour les résidus normalisés
plt.plot([np.min(t), np.max(t)], [-2, -2],'r')   
plt.plot([np.min(t), np.max(t)], [2, 2],'r')
plt.xlabel(" t en s")
plt.ylabel("Écarts normalisés")
plt.grid()
plt.show()

"""

