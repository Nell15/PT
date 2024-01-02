import matplotlib.pyplot as plt # bibliotheques
from math import sqrt
import csv

def lecture_listes(nom):
    liste = []
    with open(nom, newline='') as fichier:
        reader = csv.reader(fichier,delimiter=';')
        for ligne in reader:
            liste.append(ligne)
    return liste

def lecture(nom):
    with open(nom, newline='',encoding='utf-8-sig') as fichier:
        lecture = csv.DictReader(fichier, delimiter=';')
        return list(lecture)

dicos_pokemon = lecture('poke_gen9.csv')

liste_types = []
for pokemon in dicos_pokemon:
    if pokemon['type1'] not in liste_types:
        liste_types.append(pokemon['type1'])

n = len(liste_types)
N = len(dicos_pokemon)

graphes = [ [[],[],[]] for _ in range(n)]
cat = ['att', 'def', 'vit']
for pokemon in dicos_pokemon:
    for i in range(18):
        if pokemon['type1'] == liste_types[i]:
            for element in cat:
                graphes[i][cat.index(element)].append(int(pokemon[element]))

cibles = [{'nom': 'Hippodocus', 'pv': 108, 'att': 112, 'def': 118, 'vit': 47},
{'nom': 'Profissor', 'pv': 95, 'att': 50, 'def': 100, 'vit': 75},
{'nom': 'Larvax', 'pv': 55, 'att': 78, 'def': 65, 'vit': 31},
{'nom': 'Neuneuch', 'pv': 80, 'att': 98, 'def': 25, 'vit': 49},
{'nom': 'KraKreKri', 'pv': 66, 'att': 66, 'def': 66, 'vit': 66}]

from mpl_toolkits import mplot3d
fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
for i in range(18):
    x,y,z=graphes[i][0], graphes[i][1], graphes[i][2]
    ax.scatter(x, y, z, label=liste_types[i])
for cible in cibles:
    ax.scatter(cible['att'], cible['def'], cible['vit'], s=50, color='black')
ax.set_xlabel('att')
ax.set_ylabel('def')
ax.set_zlabel('vit')
plt.title(str(N)+' Pokemons par type (att, def, vit)')
plt.legend()
plt.savefig('poke.png')
plt.show()