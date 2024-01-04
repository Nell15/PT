# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt



"""
                                    Initialisation
"""

Nx = 100
Ny = 100

V = np.zeros((Ny,Nx))
B = np.zeros((Ny,Nx),dtype=bool)
# La commande crée un tableau de Ny lignes et Nx colonnes remplies de False (tableau pleins de 0, 0 convertis en False)

#initialisation des bords et de la grille à V0
def initialisation_contour(V0):
    #QC1 :compléter   
    # bord bas :
    B[0,:] = True
    V[0,:] = V0
    # bord haut :
    B[Ny - 1,:] = True
    V[Ny - 1,:] = V0
    # bord gauche :
    B[:,0] = True
    V[:,0] = V0
    # bord droit :
    B[:,Nx - 1] = True
    V[:,Nx - 1] = V0

def  initialisation_condensateur(Vhaut,Vbas,L,e):
    #QC2 :compléter 
    ihaut = (Ny-e)//2
    ibas = (Ny+e)//2
    jgauche= (Nx-L)//2
    jdroit = (Nx+L)//2 + 1 #exclus
    B[ihaut, jgauche:jdroit] = True
    V[ihaut, jgauche:jdroit] = Vhaut
    B[ibas, jgauche:jdroit] = True
    V[ibas, jgauche:jdroit] = Vbas
 
"""
                                    Méthode de Jacobi
"""  
 
#itération de Jacobi
def iteration_jacobi():
    # QC3 compléter 
    oldV = V.copy()
    eSum = 0
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            if B[i,j] == False: # Note : 0 marche à la place de False
                V[i,j] = (oldV[i+1, j] + oldV[i-1, j] + oldV[i, j+1] + oldV[i, j-1]) / 4
                eSum += (V[i,j] - oldV[i, j]) ** 2
                # ...... ?
                
    e = np.sqrt(eSum / (Nx * Ny))
    return e 
   
# 7: car l'égalité aurait fait de oldV un tableau muable lié à V or on souhaite conserver une version non modifiée
# du tableau V 

#boucle de résolution de Laplace
def jacobi(eps):
    e = 3 * eps 
    i = 0   # compteur d'itérations
    # QC4 compléter 
    while e > eps:
        e = iteration_jacobi()
        i += 1
        if i%10 == 0:
            print(e)
        # compléter 
    return i

"""                        "Outil graphique de tracer 
""" 

#trace les bords du domaine et les équipotentielles
def trace_equipot():
    
    plt.figure()
    x = np.arange(0, Nx, 1)
    y = np.arange(0, Ny, 1)
    
    plt.imshow(B,cmap='binary',origin='lower')
    
    nb_equipot1 = 16 # nombre d'equipotentielles
    nb_equipot2 = 100
    
    # QC6  utiliser plt.contour
    plt.contour(x, y, V, nb_equipot1,cmap='binary')
    # QC7 compléter
    plt.contourf(x, y, V, nb_equipot2, cmap='coolwarm',origin='lower')
    plt.colorbar()
    plt.show()

"""
                      MÉTHODE DE GAUSS-SEIDEL adaptative
""" 
'''
def iteration_gauss_seidel():
    w = 2 / (1 + np.pi / Ny)
    # QC8 compléter 
    for i in range(Nx):
        for j in range(Ny):
            if B[i,j] == False:
                oldV = V.copy()
                V[i,j] = 
                ......
                ........
    return e


def gauss_seidel(eps):
    def jacobi(eps):
        e = 3*eps 
        i = 0   # compteur d'itérations
        QC9 compléter 
        while .....
            ....
             compléter 
        return i
'''


"""                                    code général
"""  


Nx = 100
Ny = 100

V = np.zeros((Ny,Nx))
B = np.zeros((Ny,Nx),dtype=bool)

# à compléter 
initialisation_contour(0)
initialisation_condensateur(15, -15, 30, 35)

jacobi(10 ** -3)     #calcul  avec Jacobi

#gauss_seidel(???)   #calcul  avec Gauss-Seidel

trace_equipot()