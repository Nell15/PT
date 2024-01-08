"""
@author: ntruong
"""

from random import *

def lancer()->int:
    return randint(1, 6)

def liste(n:int)->list:
    return [lancer() for i in range(n)]

def arrivee(k:int, L:list)->int:
    n = len(L)
    while k + L[k] < n:
        k += L[k]
    return k

def commun(L:list):
    pass



## Tests:

L_sujet = [3, 6, 1, 4, 5, 4, 2, 4, 5, 6, 5, 3, 2, 1, 2, 6, 1, 3, 5, 1]
# print(arrivee(2, L_sujet))

# for n in [15, 20, 25]:
#     print("Test pour k =", n)
#     test = liste(25)
#     for k in range(len(test)):
#         print("Départ case", k, "donne", arrivee(k, test))
#     print()

# Que constatez vous ? : on arrive toujours sur une des 5 dernières cases :')