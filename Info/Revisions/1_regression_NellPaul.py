"""
@author: ntruong, prichert
"""

import matplotlib.pyplot as plt

def moyenne(l:list)->float:
    return sum(l) / len(l)

def var(l:list)->float:
    return sum([(l[i] - moyenne(l)) ** 2 for i in range(len(l))]) / len(l)

def covar(l:list, m:list)->float:
    """Calcule la covariance de deux listes de longueurs égales."""
    return sum([(l[i] - moyenne(l)) * (m[i] - moyenne(m)) for i in range(len(l))]) / len(l)

def regression(l:list, m:list)->tuple:
    a:float = covar(l, m) / var(l)
    b:float = moyenne(m) - a * moyenne(l)
    return a, b

tps_revision = [1, 2, 2.5, 3, 4, 4.5, 5, 6]
note = [5, 10, 12, 15, 10, 15, 13, 17]

a, b = regression(tps_revision, note)

n = 15 # nombre arbitraire
ordonnees = [a * i + b for i in range(n)]
abscisses = [*range(n)]

plt.clf()
plt.plot(abscisses, ordonnees, color="dodgerblue")
plt.scatter(tps_revision, note, color='r')
plt.show()

def estimation(t:float)->float:
    a, b = regression(tps_revision, note)
    return a * t + b

## Tests

liste_l_ref:list = [0, 1, 2]
liste_m_ref:list = [3, 4, 5]

print(f"Moyenne de {liste_l_ref}:", moyenne(liste_l_ref))
print(f"Variance de {liste_l_ref}:", var(liste_l_ref))
print(f"Covariance de {liste_l_ref} et {liste_m_ref}:",covar(liste_l_ref, liste_m_ref))
print("Coefficients de la régression (a, b):",regression(liste_l_ref, liste_m_ref))
print("Estimation pour 7 heures de travail: Note =", estimation(7))