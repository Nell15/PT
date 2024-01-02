# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 08:14:59 2023
@author: mhebding
@title: theorie des jeux
"""

# Modelisation du jeu
# 1.
def affiche_configuration(c):
    k, joueur = c
    print("C'est au joueur J{} de jouer, il y a {} allumette(s) sur la table.".format(joueur,k))
    return

# 2.
def liste_coups_suivants(c):
    k, joueur = c
    L = []
    for p in range(1, min(3, k)+1): # le joueur prend p allumettes (1 <= p <= 3,k)
        L.append((k-p, 1-joueur))
    return L

# Algorithme min-max avec heuristique
# 3.
def h(c):
    k, joueur = c
    if k == 0 and joueur == 0: # si configuration finale gagnÃ©e par J0
        return 1
    elif k == 0 and joueur == 1: # si configuration finale gagnÃ©e par J1
        return -1
    else: # si configuration finale nulle ou configuration non finale
        return 0
    
# 4.    
def minmax(c, h, p): # algorithme minmax avec heuristique
    k, joueur = c
    if k == 0 or p == 0: # si configuration finale ou profondeur nulle
        return h(c)
    else:
        coups=liste_coups_suivants(c)
        H = [minmax(s, h, p-1) for s in coups]
        if joueur == 0: # si joueur MAX
            return max(H)
        else: # si joueur MIN
            return min(H)
        
# for i in range(10):
#     print(minmax((i, 0), h, 2))

# 5.1        
def XminimisantY(X, Y):
    #return X[Y.index(min(Y))]
    imin = 0 # indice du minimum
    for i in range(1,len(X)):
        if Y[i] < Y[imin]:
            imin = i
    return X[imin]

# 5.2
def XmaximisantY(X, Y):
    #return X[Y.index(max(Y))]
    imax = 0 # indice du maximum
    for i in range(1, len(X)):
        if Y[i] > Y[imax]:
            imax = i
    return X[imax]

# 5.3
def coup_suivant_par_minmax(c,h,p):
    k, joueur = c
    coups_suivants = liste_coups_suivants(c)
    if joueur == 0: # si joueur MAX
        return XmaximisantY(coups_suivants, [minmax(coup, h, p) for coup in coups_suivants])
    else: # si joueur MIN
        return XminimisantY(coups_suivants, [minmax(coup, h, p) for coup in coups_suivants])
 
# 6.
def joue(n, h, p):
    c = (n, 0) # configuration initiale
    print("Vous Ãªtes le joueur J0.")
    while c[0] > 0: # tant que la partie n'est pas terminÃ©e
        k, joueur = c
        if joueur == 0: # si c'est au joueur J0 de jouer
            affiche_configuration(c)
            meilleur_coup = coup_suivant_par_minmax(c,h,n)
            print("Votre meilleur coup Ã  jouer est de prendre "+ str(k-meilleur_coup[0]) +" allumette(s).")
            nbre_enleve = int(input("Combien d'allumette(s) souhaitez-vous enlever ? "))
            assert nbre_enleve in [1, 2, 3] # prÃ©vention contre la triche
            c = (k-nbre_enleve, 1) # configuration suivante
        else:
            affiche_configuration(c)
            meilleur_coup = coup_suivant_par_minmax(c, h, p)
            print("Le joueur J1 enlÃ¨ve " + str(k-meilleur_coup[0]) + " allumette(s).")
            c = meilleur_coup
    joueur = c[1] # joueur contrÃ´lant la configuration finale
    print("Le joueur J" + str(joueur) +" a gagnÃ© !")
    
# 7.   
"""
L'ordinateur sera imbattable si p = n.
"""

# Cas oÃ¹ l'ordi gagne...
n = 21
p = n
#joue(n, h, p)

# A p=8, l'ordi peut perdre :)
p = 8
#joue(n, h, p)

# Remarque :
"""
ConsidÃ©rons la stratÃ©gie suivante (qui est bien positionnelle, mÃªme si nous ne l'exprimons pas ainsi),
consistant Ã  prendre un nombre d'allumettes tel que la somme des allumettes prises par le joueur
prÃ©cÃ©dent et le joueur actuel soit Ã©gale Ã  4.
Alors sur deux tours, le nombre d'allumettes dÃ©croÃ®t de 4 unitÃ©s.
Ainsi si initialement n = 4k + 1, le joueur qui joue en second peut s'assurer que le premier joueur
a toujours face Ã  lui un nombre d'allumettes Ã©gal Ã  1 modulo 4, et le premier joueur finit par devoir
tirer la derniÃ¨re # allumette, perdant ainsi le jeu. Le second joueur a donc une stratÃ©gie gagnante.

A contrario si n <> 4k+1, le premier joueur peut prendre un nombre d'allumettes de sorte que le nombre
d'allumettes restantes soit Ã©gal Ã  1 modulo 4. C'est alors le second joueur qui se trouvera toujours
face Ã  un nombre d'allumettes Ã©gal Ã  1 modulo 4, et qui finira par tirer la derniÃ¨re allumette.
C'est maintenant le joueur qui commence qui a une stratÃ©gie gagnante.
"""