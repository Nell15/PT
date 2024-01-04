
"   FFT-sinus-echantillonne- El .py"
from scipy.fftpack import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt


f= 3e3 # Fréquence du signal

#  Création du signal
# QC1 : coder la fonction  x(t)= sin (2 πft) 
def x(t):
    return np.sin(2 * np.pi * f * t)

# Échantillonnage du signal
fe=10e3  # fréquence d'échantillonnage (Hz)
Te = 1/fe  # Période d'échantillonnage en seconde
N=1024      #  Nombre de points 


# QC7 calcul de la durée D en focntion de (N,fe)   #  durée 

Te = 1 / fe
D = N * Te

# QC3  créer te avec linspace   # Temps des échantillons
te = np.linspace(0, D, N)
xe = x(te)

"                                 Spectre du signal "
# Calcul FFT
# QC9   calcul de la FFt de x(t)  # Transformée de fourier

X = fft(xe)

# Fréquences de la transformée de Fourier par calcul direct
# QC10 calcul de  freq1
freq1 = 1 / D * np.arange(N)

# QC11  normalisation des amplitudes notés  X1 
X1 = 2 / N * abs(X)

# Fréquences de la transformée de Fourier par FFTfreq
# QC12 récupération de   freq avec  fftfreq
freq = fftfreq(N, Te)

# QC13  On garde uniquement les fréquences positives

freq2 = freq[:N // 2]

# QC14   Mise en forme des amplitudes associées

X3 = 2 / N * abs(X[:N // 2])



# Tracé du spectre avec calcul direct
plt.figure()
plt.plot(freq1*1e-3 ,X1)
plt.xticks(np.arange(0, 11, 1)) #graduation de l'axe x
plt.grid()
plt.xlabel(r"Fréquence (kHz)")
plt.title("calcul direct")

#Tracé du spectre avec FFTfreq
plt.figure()
plt.plot(freq2*1e-3, X3)
plt.xlim(0, 10)  # On réduit la plage des fréquences à la zone utile
plt.xticks(np.arange(0, 11, 1))
plt.xlabel(r"Fréquence (kHz)")
plt.grid()
plt.title("avec FFTfreq")

plt.show()