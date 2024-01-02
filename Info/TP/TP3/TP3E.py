## PROGRAMMATION DYNAMIQUE ##
from math import inf
import numpy as np

## RENDU DE MONNAIE 

# 1. 
# Reponse a la question 1.
reponse1 : str = "cette résolution donne une piece de 10 ct, on perds 1 ct"

# 2. 
# Reponse a la question 2.
reponse2 : str = "oui, une pièce de 5 ct et 3 pièces de 2ct"

# 3. 
# Reponse a la question 3.
réponse3 : str = "non, pas toujours *2"

# 4. 
# https://media.discordapp.net/attachments/914515328510353458/1061923621762760724/IMG_20230109_092504.jpg?width=1245&height=700

# 5.
euros : list = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(systeme, somme):
    monnaie : list = []
    for piece in systeme:
        while somme >= piece:
            somme -= piece
            monnaie.append(piece)
    return monnaie if somme == 0 else None

# print(rendu_glouton(euros, 16))

# 6.
def rendu_recursif(systeme, somme):
    if somme < 0:
        return inf
    elif somme == 0:
        return 0
    minimum = inf
    for x in systeme:
        if somme >= 0:
            minimum = min(minimum, 1 + rendu_recursif(systeme, somme - x))
    return minimum

# print(rendu_recursif(euros, 16))
# print(rendu_recursif(euros, 16)) # Note : trop long a executer pour 48

# 7. 8.
def rendu_memoise(systeme, somme):
    f : list = [0] * (somme + 1)
    for s in range(1, somme + 1):
        f[s] = inf
        for x in systeme:
            if s >= x:
                if 1 + f[s - x] < f[s]:
                    f[s] = 1 + f[s - x] # MAJ du minimum
    return f[somme]
    # return f # si on veux retourner le tableau de mémoisation

print(rendu_memoise(euros,16))

# 9. 
# Reponse a la question 9.
reponse9 : str = "c'est le nombre de pieces minimum nécessaire au rendu de la somme d'entrée"
# 10. 
# Longue reponse a la question 10.

# 11. 
# Arbre de decisions a faire sur papier.
#https://media.discordapp.net/attachments/914515328510353458/1059780074125148170/IMG_20230103_112721.jpg?width=1245&height=700

# 12. 
def rendu_memoise_reconstitue(systeme, somme):
    f : list = [0] * (somme + 1)
    g : list = [0] * (somme + 1)
    for s in range(1, somme + 1):
        f[s] = inf
        for x in systeme:
            if s >= x:
                if 1 + f[s - x] < f[s]:
                    f[s] = 1 + f[s - x] # MAJ du minimum
                    g[s] = s - x # on retient d'où l'on vient
    monnaie = []
    while somme > 0:
        monnaie.append(somme - g[somme])
        somme = g[somme]
    return len(monnaie), monnaie
    # return f # si on veux retourner le tableau de mémoisation

#print(rendu_memoise_reconstitue(euros,16))

## LE PROBLEME DU SAC A DOS

# Introduction : 

# Reponse aux questions d introduction
rep_intro : str = """
Algo glouton : Il prendra 8 portes-clés.
Le choix est optimal.
Il lui faudra un bon moment ^^"""
# 13.
# Reponses a la question 13.
rep13 : str = """Si P = 0, on a par convention V(i, P) = 0
si i = 0, on a V(i, P) = v0 * (P // p0)"""

# 14.
# Longue reponse a la question 14.

# 15.
def sacADos(poids:list, valeurs:list, capacite:int):
    N = len(poids)
    # V = [[0] * (capacite + 1)] * (N + 1)
    V = np.full((N + 1, capacite + 1), 0)
    for i in range(1, N + 1):
        for p in range(1, capacite + 1):
            if poids[i - 1] <= p:
                V[i][p] = max(V[i - 1][p], valeurs[i - 1] + V[i - 1][p - poids[i - 1]])
            else:
                V[i][p] = V[i - 1][p]
    # "afficher le tableau"
    print(V)
    return V[N][capacite]


noms = ['porte-cles', 'livre', 'parchemins', 'calculatrice']
poids = [1,5,3,4]
valeurs = [15,10,9,5]

print(sacADos(poids, valeurs, 8))
# Tableau a remplir a la main sur papier.

# 16.
# Reponse a la question 16.

# 17.
# tableau = sacADos(poids, valeurs, 8)

def solutionSac(V, poids, valeurs):
    # FONCTION A ECRIRE
    pass

#print(solutionSac(tableau, poids, valeurs))