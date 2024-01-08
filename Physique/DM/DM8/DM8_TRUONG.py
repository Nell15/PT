import numpy as np
import matplotlib.pyplot as plt

# Initialisation des variables
g = 9.81
alpha = 10e-3
dt = 0.1 # pas de temps (en s)

# Initialisation des listes de temps T et de hauteur H
T = [0]
H = [1.5]

# Initialisation des valeurs courantes de hauteur et temps
tk = T[0]
hk = H[0]

# BOucle de calcul
while hk > 0:
    # Actualisation des valeurs courantes tk et hk
    hk += -alpha * np.sqrt(2 * g * hk) * dt
    tk += dt
    # Actualisation des listes T et H
    H.append(hk)
    T.append(tk)

plt.clf()
plt.plot(T, H, 'r')
plt.grid()
plt.show()