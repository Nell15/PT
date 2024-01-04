"                                       filtragenumerique-sinus-El.py"
import matplotlib.pyplot as plt
import numpy as np

#Méthode d'Euler 

QC16:  fonction  euler_ordre_1_passe_bas(ve, fe, fc)



## Sinusoïde
  QC17 fonction  sinusoide(f,t)
   

def trace_sinusoide(f,fe, fc):

	T = 1/f
	D = 10*T #Durée
	N = int((D*fe)+1)
	t = []
	ve = []
     QC18  remplir les listes t et ve
     
     #Tracer de la sinusoide 
	QC19  tracer  ve=f(t) en rouge 
    
	QC20 appeler  euler
    
    #Tracer de la réponse du filtre 
    QC21 :  tracer  vs=f(t) en bleu
	plt.xlabel('temps en s')
	plt.ylabel('tension en V')
    
	QC22 mettre la légende ve et vs



plt.figure() # ouvre une nouvelle figure
trace_sinusoide(1e3,100e3,1e3)
plt.show()
