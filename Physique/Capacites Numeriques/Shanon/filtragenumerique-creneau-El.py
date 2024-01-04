"                    filtragenumerique-creneau-El.py"

import matplotlib.pyplot as plt
import numpy as np

QC23:  fonction  euler_ordre_1_passe_bas(ve, fe, fc)



## Créneau
def creneau(f,t):
    return 2*(int(2*f*t)%2)-1
   

t=[]
ve=[]
fe=100e3

f=1000
T=1/f
D = 2*T  #duree
N=int((D*fe)+1)
 
 QC24  remplir les listes t et ve
    

plt.figure() # ouvre une nouvelle figure
 QC25  tracer  ve=f(t) en rouge 
 
 QC26 écrire le code correspondant au tracer qui doit 
  - appeler la fonction  euler_ordre_1_passe_bas(ve, fe, fc) 
    pour les différents situations
   - superposer les courbes avec des couleurs différentes
 - Mettre des  légendes 







