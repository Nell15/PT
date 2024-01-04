#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DM1 PT 2021
@author: TRUONG - Nell
"""
# DM1 - Informatique PT 2022/23

import numpy as np

def cs_max(nombres:tuple)->int:
    """Fonction auxiliaire permettant le calcul du nombre de chiffres
    significatifs d'un flottant. Sert pour approximer les valeurs dans 
    la fonction deplacerParticule(), car les opérations sur les flottants 
    engendrent des résidus lors des calculs."""
    CS = []
    for nb in nombres:
        s_nombre = str(nb)
        if "." in s_nombre:
            decimales = s_nombre.split(".")[1]
            CS.append(len(decimales))
        else:
            CS.append(0)
    return max(CS)

# Question 1
def deplacerParticule(particule:tuple, largeur:int, hauteur:int):
    """Prends en entrée les paramètres d'une particule
    et les dimensions de la zone d'étude à un instant t.
    Retourne les paramètres de la particules à t + 1"""
    x, y, vx, vy = particule
    cs = cs_max(particule)
    # on modifie la vitesse de la particule si un bord est atteint
    if x + vx >= largeur or x + vx <= 0:
        vx *= -1
    if y + vy >= hauteur or y + vy <= 0:
        vy *= -1
    # on arrondit pour éviter les résultats comme 2.3000000000000003
    x = round(x + vx, cs)
    y = round(y + vy, cs)
    return (x, y, vx, vy)

# Question 2
def nouvelleGrille(largeur:int, hauteur:int):
    """Prends en entrée les dimensions d'une grille
    Retourne un tableau de même dimensions, rempli de None"""
    return np.full((hauteur, largeur), None)

# Question 3
def majGrilleOuCollision(grille):
    """Prends en entrée une grille et la retourne à l'instant suivant
    si aucune collision n'a lieu. Retourne None sinon."""
    hauteur, largeur = len(grille), len(grille[0])
    nvGrille = nouvelleGrille(largeur, hauteur)
    # on regarde chaque case de notre grille
    for ligne in grille:
        for colonne in ligne:
            # si une particule s'y trouve
            if colonne != None:
                particule = colonne
                nx, ny, nvx, nvy =  deplacerParticule(particule, largeur, hauteur)
                nvCase = int(nx), int(ny)
                # on regarde si sa position dans la nouvelle grille est disponible
                # si oui, on continue
                if nvGrille[nvCase] == None:
                    nvGrille[nvCase] = (nx, ny, nvx, nvy)
                # si non, il y a collision
                else :
                    return None
    return nvGrille

# Question 4
def attendreCollisionGrille(grille, tMax:int):
    """Prends en entrée les dimensions d'une grille et tmax un entier
    Retourne le temps auquel on a collision si cela survient avant tmax,
    None sinon."""
    t = 1
    nvGrille = majGrilleOuCollision(grille)
    # permet de vérifier si on a ou non collision
    if not isinstance(nvGrille, np.ndarray):
        collision = True
    else:
        collision = False
    while not collision and t <= tMax:
        t += 1
        nvGrille = majGrilleOuCollision(nvGrille)
        if not isinstance(majGrilleOuCollision(nvGrille), np.ndarray):
            collision = True
        else:
            collision = False
    return t if collision else None

# Question 5
# O(tmax* hauteur * largeur)
  
# Question 6
RAYON = 0.2 # valeur arbitraire et constante

def detecterCollisionEntreParticules(p1:tuple, p2:tuple):
    """Prends en entrée deux particules
    Retourne True si elles sont en collision, False sinon."""
    x1, y1, vx1, vy1 = p1
    x2, y2, vx2, vy2 = p2
    dx, dy = x1 - x2, y1 - y2
    if np.sqrt(dx ** 2 + dy ** 2) <= 2 * RAYON:
        return True
    else:
        return False

# Question 7
def maj(particules:tuple):
    """Prends en entrée un tuple de forme : 
    (largeur, hauteur, listeParticules)
    Retourne un tuple de même forme à l'instant suivant"""
    largeur, hauteur, listeParticules = particules
    nvListeParticules = []
    for particule in listeParticules:
        nvListeParticules.append(deplacerParticule(particule, largeur, hauteur))
    return (largeur, hauteur, nvListeParticules)

# Question 8  
def majOuCollision(particules:tuple):
    """Prends en entrée un tuple de forme : 
    (largeur, hauteur, listeParticules) et le retourne à l'instant suivant
    si aucune collision n'a lieu. Retourne None sinon."""
    largeur, hauteur, listeParticules = particules
    largeur, hauteur, nvListe = maj(particules)
    # on regarde chaque couple de particules possible
    for i in range(len(nvListe)):
        for j in range(i + 1, len(nvListe)):
            p1, p2 = nvListe[i], nvListe[j]
            # si il y a collision
            if detecterCollisionEntreParticules(p1, p2):
                return None
    return largeur, hauteur, nvListe

# Question 9
def attendreCollision(particules:tuple, tMax:int):
    """Prends en entrée un tuple de forme 
    (largeur, hauteur, listeParticules) et tmax un entier
    Retourne le temps auquel on a collision si cela survient avant tmax,
    None sinon."""
    t = 1
    nvListe = majOuCollision(particules)
    # permet de savoir si on a eu collision ou non
    if not isinstance(nvListe, tuple):
        collision = True
    else:
        collision = False
    while not collision and t <= tMax:
        t += 1
        nvListe = majOuCollision(nvListe)
        if not isinstance(majOuCollision(nvListe), tuple):
            collision = True
        else:
            collision = False
    return t if collision else None

# COMPLEXITE : O(tmax * n * (n + 1) / 2)

# Question 10
# La distance entre les deux particules doit au maximum être de 
# 2 * rayon + 2 * vmax

# Question 11
VMAX = 1.0 # valeur arbitrairement choisie, constante

def majOuCollisionX(particules:tuple):
    """Prends en entrée un tuple de forme : 
    (largeur, hauteur, listeParticules) et le retourne à l'instant suivant
    si aucune collision n'a lieu. Retourne None sinon."""
    largeur, hauteur, listeParticules = particules
    largeur, hauteur, nvListe = maj(particules)
    for i in range(len(listeParticules)):
        for j in range(i + 1, len(listeParticules)):
            p1, p2 = listeParticules[i], listeParticules[j]
            x1, y1, vx1, vy1 = p1
            x2, y2, vx2, vy2 = p2
            dx, dy = x1 - x2, y1 - y2
            # si les particules sont trop éloignées pour pouvoir entrer en collision
            if np.sqrt(dx ** 2 + dy ** 2) > 2 * RAYON + 2 * VMAX:
                break
            # sinon, si elles entrent en collision
            elif detecterCollisionEntreParticules(nvListe[i], nvListe[j]):
                return None
    return largeur, hauteur, nvListe

## FIN
