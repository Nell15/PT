"""
@author:ntruong
"""

import numpy as np
from random import randint

def proportion(g):
    """Retourne la proportion de 0 dans une grille.
    ie: nombre de 0 / nombre total de cases"""
    return (np.size(g) - np.count_nonzero(g)) / np.size(g)

def grille_aleatoire(n:int, p:int, k:int):
    """Génère une grille de taille n*m 'pleine' de 0 et contenant k 1 à des emplacements aléatoires."""
    grille = np.zeros((n, p))
    for i in range(k):
        grille[randint(0, n-1)][randint(0, p-1)] = 1
    return grille

def voisins(g, i:int, j:int):
    """Retourne le nombre de bombes voisines à la case de coordonées (i, j)."""
    n, p = len(g), len(g[0])
    droite = True if j < p-1 else False
    gauche = True if j > 0 else False
    haut = True if i > 0 else False
    bas = True if i < n-1 else False
    nb_voisins = 0
    if droite:
        if g[i][j+1] == 1:
            nb_voisins += 1
        if bas:
            if g[i+1][j+1] == 1:
                nb_voisins += 1
        if haut:
            if g[i-1][j+1] == 1:
                nb_voisins += 1
    if gauche:
        if g[i][j-1] == 1:
            nb_voisins += 1
        if bas:
            if g[i+1][j-1] == 1:
                nb_voisins += 1
        if haut:
            if g[i-1][j-1] == 1:
                nb_voisins += 1
    if bas:
        if g[i+1][j] == 1:
            nb_voisins += 1
    if haut:
        if g[i-1][j] == 1:
            nb_voisins += 1
    return nb_voisins

def demineur(g):
    """Retourne la grille du démineur associée à la grille g."""
    g1 = np.full((len(g), len(g[0])), " ")
    for i in range(len(g)):
        for j in range(len(g[0])):
            g1[i][j] = str(voisins(g, i, j)) if g[i][j] != 1 else "M"
    return g1

# Note, les chiffres n'étant pas imposés d'être des int on utilise des str pour utiliser facilement 
# des tableaux numpy, facilitant l'utilisation des tableaux.

## Tests

n, p, k = 10, 10, 5
# Valeurs arbitraires modifiables à souhait
print(demineur(grille_aleatoire(n, p, k)))