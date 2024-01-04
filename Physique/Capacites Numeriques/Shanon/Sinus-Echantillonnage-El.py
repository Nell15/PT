"     Sinus-Echantillonage-El.py"
import numpy as np
import matplotlib.pyplot as plt

# Signal
f=10e3  # fréquence du signal (Hz)

#  Création de la sinusoide
# QC1 : coder la fonction  x(t)= sin (2 πft) 
def x(t):
    return np.sin(2.0 * np.pi * f * t)

# Paramètes Echantillonnage
D = 0.5e-3  # Duree d'observation (s)
fe = 15e3   # Frequence d'echantillonnage (Hz)
# QC2 : calcul de N    # Nombre de points enregistres

N = int(D * fe)

# création des tableaux de temps 
#  QC3 créer te avec linspace    # Grille d'echantillonnage

te = np.linspace(0.0, D, N + 1)
# Grille plus fine pour tracer l'allure du signal parfait
# QC4 créer t avec linspace pour 2000 éléments  

t = np.linspace(0.0, D, 2000)

# Trace du signal
plt.plot(te * 1e3, x(te), 'ro-', label = "fe=200kHz")
# plt.plot(te * 1e3, x(te), 'ro-', label = f"fe={fe}KHz")
plt.plot(t * 1e3, x(t), 'dodgerblue', label = '2000 points')
plt.grid()
plt.xlabel("t (ms)")
plt.ylabel("Amplitude x(t)")
plt.legend(loc = 'upper right')
plt.show()

valeurs_cours_fe = [200e3, 50e3, 15e3, 4.5e3]