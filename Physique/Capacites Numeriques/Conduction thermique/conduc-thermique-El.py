# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

"""
   #####  Valeurs  ######
"""

conductivite=250    #conductivite thermique 
Psurf=2000          #Puissance surfacique 

a=0.02              #(en m) 
b=0.01              #(en m) 
S=a*b               #section de la barre
conductivite=237    #conductivite thermique aluminium
rho=2699            #masse volumique
c=897               #capacité thermique massique


h=1600              #coefficient d'échange barre-air
Tair=20             #temperature de l'air
P=11                #puissance thermique de la résistance chauffante

D = 0.005           #diffusivité
L = 1.0             # Longueur de la barre (en m) 

tmax = 295          #date de fin d'intégration

N = 101             #nombre de points pour la discrétisation spatiale
M = 30000           #nombre de dates (0 excepté) pour la discrétisation temporelle



# QC1  calcul pas spatial dx
dx : float = L / N
# QC2  calcul pas temporel dt
dt : float = tmax / M
# QC3  calcul de alpha

alpha : float = D * dt / (dx ** 2)
print('alpha: ', alpha)
print('Echelle temporelle caractéritique: ', L **2 / D)


if alpha>0.5:
    raise Exception('alpha>0.5 !')
# cette ligne permet de ne pas éxécuter le code si on releve une valeur hors cas d'utilisation

"""
#####  Initialisations ##### 
"""
# tableau des abscisses:
# QC4  crééer x avec np.linspace
x = np.linspace(0, L, N)

T = np.zeros((N))
#ajout est le tableau des quantités à ajouter à T(t_n) pour obtenir T((t_n+1) 
ajout = np.zeros((N))

#Condition initiale
Tinit = 25  #valeur initial de la paroi en tous points

# QC5 : initialiser la tableau de température T à Tinit 
T[:] = Tinit
print(T)

#tracé de T(x) à la date t=0
# QC6 :  code permettant de tracer T=f(x) à t=0 
plt.plot(x, T, label='Temperature fonction de x à t = 0')
plt.show()

"""
      ####################################################################
"""

"""
 ###########      conduction thermique avec conditions de Dirichlet    #####
"""

"""
Tx0=50    # valeur en x=0
TxL=10    # valeur en x=L 

#conditions aux limites
def T0(t):  #QC6
    # if t <= 0:
    #     return Tx0
    # else:
    #     return T0(t - dt + 1)
    return Tx0 #??????????????
 
def TL(t):  #QC7
    return TxL #??????????????

# boucle temporelle
for n in range(1,M):
    for j in range(1,N-1):
    #schéma numérique des points intérieurs
        ajout[j] = alpha * (T[j-1] + T[j+1] - 2 * T[j]) # selon [R1]
    T = T + ajout
    date = n*dt
    
    #points extrémes, Dirichlet
    T[0]=T0(date)
    T[N-1]=TL(date)

    #tracé toutes les M/10 
    if (n%(M//10) == 0):
        plt.plot(x,T, label='t(s)= '+ str(round( n*dt,1)))

#tracé solution stationnaire exacte 
Tex = np.zeros((N))
# QC10 
Tex = T[0] + (T[N-1] - T[0]) * x / L
plt.plot(x, Tex, label='Sol.statio. exacte')
plt.show()
"""

"""
      ####################################################################
"""


"""
 ###########  conduction thermique avec conditions de Dirichlet/Neumann  #####
"""

#conditions aux limites
TxL=25 # valeur en x=L 

#conditions aux limites
def TL(t): #QC11
    return TxL # ???

def jQ0(t): #QC12
    return Psurf # ???

# boucle temporelle
for n in range(1,M):
    date=n*dt
    #schéma numérique des points intérieurs
    for j in range(1,N-1):
        ajout[j] = alpha * (T[j-1] + T[j+1] - 2 * T[j])  #selon [R1]
    #ajout pour point gauche, de type Neumann
    phi_0 = -Psurf / conductivite
    ajout[0] = 2 * alpha  * (T[1] - T[0] - dx * phi_0)  #selon [R2]
    T=T+ajout
    #points extrémes, Dirichlet
    T[N-1]=TL(date)

#tracé toutes les M/10 dates
    if (n%(M//10) == 0):
        plt.plot(x,T, label='t(s)= '+ str(round( n * dt,1)))
                                           
        
#tracé solutionstationnaire exacte
Tex = np.zeros((N))
# QC14
Tex = T[N-1] + Psurf / conductivite * (L - x)
plt.plot(x, Tex,label='Sol.statio. exacte')
plt.show()

"""
      ####################################################################
"""

"""
 ###########    conduction thermique avec conditions Mixtes #####
"""

print('Patience: le temps de calcul est long...')

#conditions aux limites
def jQ0(t): #QC15
    pass

"""# boucle temporelle
for n in range(1,M):
    date=n*dt
    #schéma numérique des points intérieurs
    for j in range(1,N-1):
        ajout[j] = #???selon [R1]
    
    #ajout pour point gauche, de type Neumann
    ajout[0]= #???selon [R2]
    #ajout pour point droit, type Newton
    ajout[N-1] #???selon [R3]
    T=T+ajout
    

#tracé toutes les M/12 dates
    if (n%(M//12) == 0):
      plt.plot(x,T, label='t(s)= '+ str(round( n *dt,1)))
      
#tracé solutionstationnaire exacte
Tex = np.zeros((N))
Tex=?????   QC18
   plt.plot(?????,label='Sol.statio. exacte')"""
      


"""   ####################################################################
"""


"""
                            Mise en forme de la figure
"""
plt.xlabel('x (m)')
plt.ylabel('T (°C)',rotation=0)
plt.legend(loc=2, bbox_to_anchor=(1, 1)) # permet d'afficher les légendes hors de la figure
plt.grid()
plt.show()