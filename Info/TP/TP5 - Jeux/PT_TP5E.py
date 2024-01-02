# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 08:14:59 2023
@author: mhebding d apres L. Lang
@title: theorie des jeux
"""

# les pass sont a completer

# Modelisation du jeu
# 1.
def affiche_configuration(c:tuple):
    k, joueur = c
    print(f"C'est au joueur J{joueur} de jouer, il y a {k} allumette(s) sur la table.")

# affiche_configuration((3, 0))

# 2.
def liste_coups_suivants(c):
    k, joueur = c
    p_joueur : int = 0 if joueur == 1 else 1                        #note: version prof: p_joueur = joueur - 1 (génie moment)
    return [(k - i, p_joueur) for i in range(1, 4) if k - i >= 0]

# print(liste_coups_suivants((3, 0)))

# Algorithme min-max avec heuristique
# 3.
def h(c):
    k, joueur = c
    if k == 0:
        return 1 if joueur == 0 else -1
    else :
        return 0
    
# print(h((0, 0)))
# print(h((0, 1)))
# print(h((1, 0)))
    
# 4.    
def minmax(c, h, p): # algorithme minmax avec heuristique
    k, joueur = c
    if k == 0 or p == 0:
        return h(c)
    else:
        p_config = liste_coups_suivants(c)
        L = [minmax(config, h, p - 1) for config in p_config]
        return max(L) if joueur == 0 else min(L)
    
# for i in range(10):
#     print(minmax((i, 0), h, 2))
# print(minmax((3, 0), h, 2))

# 5.1        
def XminimisantY(X, Y):
    return X[Y.index(min(Y))]

# 5.2
def XmaximisantY(X, Y):
    return X[Y.index(max(Y))]

# 5.3
def coup_suivant_par_minmax(c,h,p):
    k, joueur = c
    coups_suivants = liste_coups_suivants(c)
    liste_minmax = [minmax(p_c, h, p) for p_c in coups_suivants]
    return XmaximisantY(coups_suivants, liste_minmax) if joueur == 0 else XminimisantY(coups_suivants, liste_minmax)

# print(coup_suivant_par_minmax((8, 0), h, 8))

# 6.
def joue(n, h, p):
    c = (n, 0) # configuration initiale
    tour = 0
    while c[0] != 0:
        affiche_configuration(c)
        if tour % 2 == 0:
            m_conf = coup_suivant_par_minmax(c, h, p - tour)
            m_coup = c[0] - m_conf[0]
            print("Indication: meilleur coup:", m_coup)
            b = int(input("Combien voulez vous enlever d'allumettes?"))
            if not(3 >= b >= 1) or c[0] < 0:
                print("Coup invalide")
            else:
                c = (c[0] - b, 1)
                tour += 1
        else:
            c = coup_suivant_par_minmax(c, h, p - tour)
            tour += 1
    print(f"Le joueur J{c[1]} a gagné")

# joue(21, h, 1)

# Avec une profondeur de 9
# joue(21, h, 9)
# Traçage du graphe ?

joue(9, h, 9)

# 7.1
rep : str = "L'ordinateur est imbattable si p = n" 

# Graphe du jeu et calcul des attracteurs
# 8.
def GA(n):
    d = dict()
    file = [(n, 0)]
    while len(file) > 0:
        c = file.pop(0)
        if c not in d:
            d[c] = liste_coups_suivants(c)
            for coup in d[c]:
                file.append(coup)
    return d

# print(GA(4)) # essayer pour n = 4 et verifier le graphe sur papier
# Graphe fait sur papier

# 9.
def attracteur(G,S0,W0):
    A = []
    tG = {t: [s for s in G.keys() if t in G[s]] for t in G.keys()} # dictionnaire du graphe transposé
    ind = {s: len(G[s]) for s in G.keys()} # dictionnaire des indices sortants du graphe G
    def parcours(t):
        """Fonction récursive qui augmente l'attracteur à partir du sommet t"""
        if t not in A:
            A.append(t)
            for s in tG[t]: # pour chaque prédécesseur s de t (on remonte le graphe)
                ind[s] -= 1 # on indique qu'on a visité ce sommet une fois depuis A
                if s in S0 or ind[s] == 0: # si s est contrôlé par J0 ou si tous les successeurs de s sont dans A
                    parcours(s)
    for t in W0:
        parcours(t)
    return A

n = 8
G = GA(n)
S0 = [c for c in G.keys() if c[1] == 0] # commenter cette ligne
# S1 est la liste des points pour lesquels c'est au joueur 0 de jouer (les contrôle)
# cette liste est issue du graphe de la partie donné par la fonction GA
W0 = [(0, 0)] # commenter cette ligne
# Le joueur 0 gagne quand il reste à son tour 0 allumettes, ie J1 a enlevé la dernière.

attr = attracteur(G, S0, W0) # calculer et afficher les attracteurs pour G, S0, W0
# print('Attracteur J0:', end=' ')
# print(attr)

# 10.
def strategie_gagnante(G,S,W):
    A = []
    joueur = S[0][1]
    tG = {t: [s for s in G.keys() if t in G[s]] for t in G.keys()} # dictionnaire du graphe transposé
    ind = {s: len(G[s]) for s in G.keys()} # dictionnaire des indices sortants du graphe G
    strategie = dict() # dictionnaire associant à tout sommet de J0 un successeur de position gagnante
    def parcours(t):
        """Fonction récursive qui augmente l'attracteur à partir du sommet t"""
        if t not in A:
            A.append(t)
            for s in tG[t]: # pour chaque prédécesseur s de t (on remonte le graphe)
                ind[s] -= 1 # on indique qu'on a visité ce sommet une fois depuis A
                if s in S or ind[s] == 0: # si s est contrôlé par J0 ou si tous les successeurs de s sont dans A
                    if s[1] == joueur:
                        strategie[s] = t
                    parcours(s)
    for t in W:
        parcours(t)
    return strategie

S1 = [c for c in G.keys() if c[1] == 1] # commenter cette ligne
# S1 est la liste des points pour lesquels c'est au joueur 1 de jouer (les contrôle)
# cette liste est issue du graphe de la partie donné par la fonction GA
W1 = [(0, 1)] # commenter cette ligne
# Le joueur 1 gagne quand il reste à son tour 0 allumettes, ie J0 a enlevé la dernière.

print('Stratégie gagnante pour J0:', end=' ')
print(strategie_gagnante(G, S0, W0)) # afficher la strategie gagnante pour J0
print('Stratégie gagnante pour J1:', end=' ')
print(strategie_gagnante(G, S1, W1)) # afficher la strategie gagnante pour J1