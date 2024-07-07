import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constantes données par le sujet :
t0 = 0          # valeur  de départ
tf = 0.025      # valeur maximale  tf=10ms)
n = 100        # nombre d'itérations


R, L, C = 1e3, 1.1 ,1e-6 #valeurs non données et posée arbitrairement pour la visualisation

alpha = R / L
beta = 1 / (L * C)

# création du tableau de temps t :
t = np.linspace(t0, tf, n + 1)

