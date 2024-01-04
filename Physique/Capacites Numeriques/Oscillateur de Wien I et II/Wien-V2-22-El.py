# -*- coding: utf-8 -*-
"""
@author: ---
Trace les tensions produites par l'oscillateur de Wien.
Trace le spectre associé.
(Utilise un schéma d'Euler explicite pour intégrer les équations.)
"""

# ------- Calcul et tracé des tensions u(t) et v(t)

import numpy as np
import matplotlib.pyplot as plt 

R = 1e3     # Ohm, resistance du filtre passe-bande
C = 100e-9  # Farad, capacité du filtre passe bande
w0 = 1/(R*C) #pulsation propre du filtre

vsat =15      # volts, tension de saturation de l’ALI

A=4  #  gain de l'amplificateur

Q=1.0/3.0  #Facteur de quamlité du filtre
B=1.0/3.0  #H0 du filtre


 #création du tableau de temps t
t0=0        #instant initial de la simulation en seconde
tfin=10.e-3    #instant final de la simulation en seconde
dt=0.01e-3    #  pas de temps en seconde 

# QC1  code permettant le calcul du nombre d’itération  n  
# (qui doit un entier) à partir de la durée temporelle d’acquisition et du pas dt
n = int(((tfin - t0) / dt))

# QC2 code  créant le tableau de temps t  à l’aide de la commande linspace 
t = np.linspace(t0, tfin, n + 1)

# créations des tableaux
v= np.empty(n)   # sortie du filtre = entrée ALi
u= np.empty(n)   #sortie de l'ALI

dv= np.empty(n)   # dérivée de v : dv/dt
ddv= np.empty(n)  # dérivée seconde de v 

# Initialisation des variables
v[0]= 0.01    # ,on initialise avec une petite perturbation   
dv[0] = 0.01  #on initialise avec une petite perturbation

# Boucle d'intégration par Euler explicite pour calculer v

h = (tfin - t0) / n

for i in range (n-1) :  
    #cacul de la déivée seconde 
    #  QC3 :selon la condition sur v(t) ,  fonction
    #      F1 ou F2  pour calculer  ddv[i]
        # QC4 récurrence d’Euler sur dv[i]
    # 4 et 3 :  
    if abs(v) < vsat / A:
        dv[i + 1] = h * ((A * B - 1) * w0 / Q * dv[i] + v[i]) + dv[i]
    else :
        dv[i + 1] = -h * w0 * (dv[i] / Q - w0 * v[i]) + dv[i]
    # QC5 récurrence d’Euler sur v[i]
    v[i + 1] = h * dv[i] + v[i]
        

# Boucle du calcul de u à la sortie de l'ALI selon saturation ou non   
for i in range (n) :
    if abs(v[i]) < vsat / A:
        u[i] = A * v[i]
    else :
        #A FINIR
        
#    QC6   écrire le code avec  boucle FOR  permettant de déterminer 
#    la valeur de la tension u à la sortie de l’ALI selon qu’il y ait 
#    saturation ou non suivant la condition sur v[i] 
   
# Graphiques 
plt.figure()

 QC7 code permettant de tracer  v=f(t) et afficher le texte ‘v sortie filtre’ 
 QC8 code permettant de tracer  u=f(t) en pointillé et d’afficher d’afficher
      le texte ‘u sortie de l’ALI’ 

plt.xlabel('t (s)')
plt.ylabel('u et v (V)')
plt.grid()
plt.legend(loc='best')
plt.show()



# ------- Calcul et tracé du spectre

from scipy.fftpack import fft, fftfreq
vL=v.size  
N = t.size

vFFT = abs(fft(v))* 2.0/N 
freq= fftfreq(vL,dt)

vFFT=vFFT[0:len(vFFT)//2] 
freq=freq[0:len(freq)//2]    
f= freq/1e3    


plt.figure()
plt.plot(f,vFFT,label="spectre de v(t)")
plt.xlim(0,8)

QC10  Écrire le code permettant de nommer  les axes (grandeurs+unités) 

plt.grid()
plt.legend(loc='best')
plt.show()