# -*- coding: utf-8 -*-
# Created on Wed Jan 11 20:06:11 2023
# @author: mhebding, ntruong
# @title: algorithme knn
print("-" * 50, "\nDM3_TRUONG", "\n" + "-" * 50)

## 1 Chat ou lapin ? 

import matplotlib.pyplot as plt # bibliotheques
from math import sqrt

table = [
['chat',2,3], ['lapin',1,5], ['chat',4,5], ['chat',5,7], ['lapin',2,10],
['lapin',1.2,8], ['chat',7,5], ['chat',3.5,4.5], ['lapin', 3, 12], ['lapin', 4.2, 13], 
['lapin', 8, 6], ['chat', 2, 4], ['chat', 3, 5], ['lapin', 3.5, 8], ['lapin', 6, 7], 
['chat', 3, 6], ['chat', 3.8, 7], ['lapin', 8, 15], ['lapin', 7, 10], ['chat', 4.5, 8],
['chat', 10, 6], ['chat', 8, 9], ['lapin', 1, 6], ['lapin', 2.5, 9], ['chat', 7, 7],
['chat', 2, 8], ['chat', 3, 7], ['lapin', 8, 7], ['lapin', 5.5, 9.5], ['chat', 5, 3],
['chat', 9, 6], ['lapin', 7, 8], ['lapin', 4, 7], ['lapin', 3, 10], ['chat', 9, 7],
['lapin', 5.5, 7.5], ['chat', 5, 9], ['lapin', 9, 9], ['lapin', 0.9, 7], ['chat', 6, 9]
] 

# 1.
def listes(table:list, classe:str):
    """Prend en entrée une table et une classe et retourne les listes 
    associées aux poids et tailles d'oreille des animaux de la classe d'entrée"""
    listePoids : list = []
    listeOreilles : list = []
    for animal in table:
        if animal[0] == classe:
            listePoids.append(animal[1])
            listeOreilles.append(animal[2])
    return listePoids, listeOreilles

# 2.
def distance_cible(donnee:list)->float: 
    """renvoie la distance euclidienne entre une donnee et la cible"""
    xDonnee, yDonnee = donnee[1], donnee[2]
    x, y = cible[0], cible[1]
    distance = sqrt((xDonnee - x) ** 2 + (yDonnee - y) ** 2) # Distance euclidienne
    return distance

### QUESTION 11 ###
def distance_M_cible(donnee:list)->float:
    """renvoie la distance de Manhattan entre une donnee et la cible"""
    xDonnee, yDonnee = donnee[1], donnee[2]
    x, y = cible[0], cible[1]
    return abs(xDonnee - x) + abs(yDonnee - y)

def distance_T_cible(donnee:list)->float:
    """renvoie la distance de Tchebychev entre une donnee et la cible"""
    xDonnee, yDonnee = donnee[1], donnee[2]
    x, y = cible[0], cible[1]
    return max(abs(xDonnee - x), abs(yDonnee - y))
######

# 3.
def k_plus_proches_voisins(table:list, cible:list, k:int)->list:
    """renvoie la liste des kppv"""
    globals()['cible'] = cible
    # Commmentez et décommentez la ligne correspondant à la distance souhaitée
    distance = sorted(table, key = lambda pt : distance_cible(pt))[:k] # distance Eulidienne
    # distance = sorted(table, key = lambda pt : distance_M_cible(pt))[:k] # distance de Manhattan
    # distance = sorted(table, key = lambda pt : distance_T_cible(pt))[:k] # distance de Tchebychev
    return distance

# 4.
def rayon(voisins)->float:
    """renvoie la distance du plus loin"""
    # On trie la liste par ordre croissant au cas où celle-ci ne serait pas triée
    voisins : list = sorted(voisins, key = lambda pt : distance_cible(pt))
    # Note que si la liste des voisins est obtenue par la fonction k_plus_proches_voisins, 
    # elle est déjà triée. L'étape précédente sert à envisager toute situation possible.
    # On regarde alors la distance du dernier élémente de la liste triée (ordre croissant)
    return distance_cible(voisins[-1])

# 5.
def population(table:list, classe:str)->int:
    """renvoie l'effectif d'une classe dans une table"""
    compteur : int = 0
    for animal in table:
        if animal[0] == classe:
            compteur += 1
    return compteur

# 6.
def max_voisins(table:list)->str:
    """renvoie la classe la plus représentée chez les ppv"""
    reprClasses : dict = {}
    for animal in table:
        reprClasses[animal[0]] = reprClasses.get(animal[0], 0) + 1
    classeMaxRepr = max(reprClasses, key=lambda k : reprClasses[k])
    return classeMaxRepr

# 7. Résolution
liste_x_1, liste_y_1 = listes(table, 'chat')
liste_x_2, liste_y_2 = listes(table, 'lapin')

cible : list = [4, 8]
k : int = 11

voisins : list = k_plus_proches_voisins(table, cible, k)
classe_cible : str = max_voisins(voisins)
print("7. : Prédiction de la classe de la cible :")
print("Sur", k, "voisins, il y a", population(voisins,'chat'), "chats et", population(voisins, 'lapin'), "lapins : la cible pourrait être un", classe_cible)
print("-" * 50)

# 8. 9. 10.
fig, ax = plt.subplots()

# On place les points de données
plt.scatter(liste_x_1, liste_y_1, color='r', label='chats') # représente les chats
plt.scatter(liste_x_2, liste_y_2, color='b', label='lapins') # représente les lapins
plt.scatter(cible[0], cible[1], color='g', label='cible') # represente la cible

# On place le cercle
rayonCible = rayon(voisins)
cercle = plt.Circle((cible[0], cible[1]), rayonCible, fill=False, ls='dotted') # A COMPLETER
ax.add_patch(cercle)

# Traçage du graphe
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()

# 11.

# Afin de tester les différentes distances, il est necessaire de commenter et decommenter les lignes 
# correspondantes dans la fonction

rep_11 : str = """Les distances euclidienne et de Manhattan donnent un chat probable, quand a Tchebychev,
on trouve une lapin. Le résultat de la prédiction paraît alors peu stable, car bien que deux méthodes 
ai donné un même résultat, on voit que le choix de la méthode peut donner résultat radicallement différent."""
print("11. :", rep_11, "\n" + "-" * 50)

liste_cibles = [
[4,8,'chat'], [6,8,'lapin'], [10, 8,'chat'], [4,6,'chat'], [4,10,'chat'], 
[6,6,'lapin'], [8,10,'chat'], [2,5,'lapin'], [8,12,'lapin'], [9,11,'chat'], 
[6,12,'lapin'], [8,8,'chat'], [2,7,'lapin'], [4,9,'lapin'], [4,6,'chat'], 
[8,10,'chat'], [2,9,'lapin'], [3,8,'chat'], [7,12,'chat'], [9,11,'chat']
]

# [6,12,'lapins'] J'ai modifié et mis lapin au lieu de lapins car sinon, à moins de gérer ce cas particulier
# on fausse la future matrice de confusion.

# 12. 
# Vrai chat = TP / Vrai lapin = TN / Faux chat = FP / Faux lapin = FN
rep_12 : str = """on prend un jeu de donné déjà classé et on demande à l'IA de diviner la classe de chaque point.
Un vrai chat est un point identifié comme un chat par l'IA et qui est effectivement un chat, un faux chat
est un point identifié par l'IA comme un chat mais qui est en fait en lapin. De même pour les lapins,
un vrai lapin est un lapin identifié comme tel et un faux lapin est un chat identifié comme un lapin."""
print("12. :", rep_12, "\n" + "-" * 50)

# 13. 
k = 7
liste_prediction = []

for x_cible, y_cible, classe_cible in liste_cibles:
    # cible = x_cible, y_cible
    # voisins_cible = k_plus_proches_voisins(table, cible, k)
    voisins_cible = k_plus_proches_voisins(table, [x_cible, y_cible], k)
    liste_prediction.append(max_voisins(voisins_cible))

# 14. 
# On prend la liste réelle comme la liste des classes des animaux dans la liste des cibles
liste_reel = [animal[2] for animal in liste_cibles]

def matrice(liste_reel:list, liste_prediction:list)->list:
    """Prend en entrée la liste d'entrainement et la liste des predictions,
    retourne la matrice de confusion résultant des predictions."""
    TP, FP, TN, FN = 0, 0, 0, 0
    for i in range(len(liste_reel)):
        if liste_reel[i] == liste_prediction[i]:
            if liste_reel[i] == 'chat':
                TP += 1
            else :
                TN += 1
        else:
            if liste_reel[i] == 'chat':
                FP += 1
            else :
                FN += 1
    return [[TP, FP], [FN, TN]]

matrice_confusion = matrice(liste_reel, liste_prediction)
# On en extrait les composantes pour s'en servir :
TP, FP = matrice_confusion[0]
FN, TN = matrice_confusion[1]

# 15. 
# Calcul du rappel.
rappel = TP / (TP + FN)
# note = 0.5555555555555556

# 16. 
# Calcul de la precision.
precision = TP / (TP + FP)
# note = 0.4166666666666667

# 17. 
# Calcul de la specificite.
specificite = TN / (FP + TN)
# note = 0.36363636363636365

# 18. 
# Calcul de la F-mesure.
F_mesure = (2 * TP) / ((2 * TP) + FP + FN)
# note = 0.47619047619047616

# Si besoin
print("Calcul des métriques:")
print("Rappel =", rappel)
print("Précision = ", precision)
print("Spéficicité =", specificite)
print("F_mesure =", F_mesure, "\n" + "-" * 50)

# 19. 
# Commentaires de conclusion.
ccl : str = """Le rappel nous informe de la quantité de vrai positifs sur la totalité des positifs, ce nombre 
est ici d'environ 0.5, sa 'réciproque' négative, la sensibilité, est elle d'environ 0.36 etc...

On remarque que la méthode des plus proches voisins, avec 7 voisins ne semble pas très efficace et on a un 
nombre important de mauvaises prédictions.

On peut alors réfléchir à un moyen de rendre la prédiction plus efficace, une première méthode serait de 
changer le nombre de voisins utilisés (k) pour la prédiction et regarder l'influence de celui-ci sur les 
métriques."""

print("19. :", ccl, "\n" + "-" * 50)

## 2 Pokemon

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

# 20.
rep_20 : str = "On utilise la fonction lecture() puisque celle ci forme une liste OrderedDict"
print("20. :", rep_20, "\n" + "-" * 50)
dicos_pokemon = lecture('pokemon.csv')

# print(dicos_pokemon)

# 21.
def pokedex(name:str)->dict:
    i : int = 0
    pokemon = dicos_pokemon[0]['nom']
    while pokemon != name:
        i += 1
        pokemon = dicos_pokemon[i]['nom']
    modelisation = {}
    fiche = ['nom', 'pv', 'att', 'def', 'vit', 'type']
    for stat in fiche:
        modelisation[stat] = dicos_pokemon[i][stat]
    return modelisation

print("Test de Pokedex():")
print(pokedex('Mucuscule'), "\n" + "-" * 50)

# 22.
def distance(pokemon1:dict, pokemon2:dict)->float:
    """Retourne la distance euclidienne entre deux pokemons
    On considère qu'on prend en entrée les MODELISATIONS des deux pokemons.""" 
    # Les noms et types n'étant pas quantifiables, la distance sera calculée à partir des 
    # autres grandeurs de la modélisation.
    distance_carree, distance_man, liste_Tchebychev = 0, 0, []
    for stat in ['pv', 'att', 'def', 'vit']:
        distance_carree += (float(pokemon2[stat]) - float(pokemon1[stat])) ** 2
        # distance_man += abs(float(pokemon2[stat]) - float(pokemon1[stat]))
        # liste_Tchebychev.append(abs(float(pokemon2[stat]) - float(pokemon1[stat])))
    distance = sqrt(distance_carree) # distance euclidienne
    # distance = distance_man # distance de Manhattan
    # distance = max(liste_Tchebychev) # distance de Tchebychev
    return distance

Carapuce, Carabaffe = pokedex('Carapuce'), pokedex('Carabaffe')
print("Test distance():")
print("La distance entre Carapuce et Carabaffe, calculée à la main, est de 30. Le code donne:")
print("distance(Carapuce, Carabaffe) =", distance(Carapuce, Carabaffe))
print("-" * 50)

def distance_cible_pokemon(pokemon:str)->float: 
    """Retourne la distance euclidienne entre un pokemon et la cible.
    On considère qu'on prend en entrée la MODELISATION d'un pokemon."""
    # Les noms et types n'étant pas quantifiables, la distance sera calculée à partir des 
    # autres grandeurs de la modélisation.
    distance_carree, distance_man, liste_Tchebychev = 0, 0, []
    for stat in ['pv', 'att', 'def', 'vit']:
        distance_carree += (float(pokemon[stat]) - float(cible[stat])) ** 2
        distance_man += abs(float(pokemon[stat]) - float(cible[stat]))
        liste_Tchebychev.append(abs(float(pokemon[stat]) - float(cible[stat])))
    distance = sqrt(distance_carree) # distance euclidienne
    # distance = distance_man # distance de Manhattan
    # distance = max(liste_Tchebychev) # distance de Tchebychev
    return distance

cible = Carapuce
print("Test distance_cible_pokemon():") # Résultat attendu = 30
print("On prend comme cible Carapuce, et on calcule la distance de Carabaffe à la cible:")
print("distance_cible_pokemon(Carabaffe) = ", distance_cible_pokemon(Carabaffe))
print("-" * 50)

# 23.
def frequence_des_types(table:list)->dict:
    """renvoie la représention des types dans la table"""
    repr_type : dict = {}
    for pokemon in table:
        repr_type[pokemon['type']] = repr_type.get(pokemon['type'], 0) + 1
    return repr_type

note : str = """Le résultat trouvé n'est pas celui donné par le sujet, néanmoins, après analyse du fichier csv 
fournit, on remarque que les certains types dans le tableau du sujet sont faussés. Prenons l'exemple du type acier :
dans le fichier on a 4 pokemons de type Acier, or le sujet nous indique qu'il y en a 5. On remarque que le mot 
acier est trouvable dans le nom du Pokemon Chrysacier. Je ne sais comment la dictionnaire du sujet a été généré, 
cependant cette erreur est aussi trouvée sur les types eau et feu, qui sont des mots trouvés dans des noms de 
Pokemons. Ainsi j'en conclu que le dictionnaire fourni est faussé et que celui qui est juste est celui généré 
par mon code."""

frequences = frequence_des_types(dicos_pokemon)
print("Test de frequence_des_types() sur la table entière:")
print(frequences, "\n")
print(note, "\n" + "-" * 50)

# 24.
def type_majoritaire(table:dict)->str:
    """Renvoie le type le plus représenté dans une table"""
    # freq = frequence_des_types(table)
    # max_repr_type = max(freq, key=lambda k : freq[k])
    max_repr_type = max(table, key=lambda k : table[k])
    return max_repr_type

print("Test de type_majoritaire() sur le résultat précédent:")
maxi = type_majoritaire(frequences)
print("Type majoritaire dans la table =", maxi) # Note : résultat attendu = Normal
print("-" * 50)

# # 25.
def knn_pokemon(table:list, nouveau:dict, k:int)->list:
    """"""
    global cible
    cible = nouveau
    nv_table = []
    for pokemon in table:
        nv_table.append(pokedex(pokemon['nom']))
    return sorted(nv_table, key = lambda pk : distance_cible_pokemon(pk))[:k]

# # 26.
cible0 = {'nom': 'Carapuce', 'pv': 44, 'att': 48, 'def': 63, 'vit': 43} # Note : type eau

cible1 = {'nom': 'Hippodocus', 'pv': 108, 'att': 112, 'def': 118, 'vit': 47}
cible2 = {'nom': 'Profissor', 'pv': 95, 'att': 50, 'def': 100, 'vit': 75}
cible3 = {'nom': 'Larvax', 'pv': 55, 'att': 78, 'def': 65, 'vit': 31}
cible4 = {'nom': 'Neuneuch', 'pv': 80, 'att': 98, 'def': 25, 'vit': 49}
cible5 = {'nom': 'KraKreKri', 'pv': 66, 'att': 66, 'def': 66, 'vit': 66}

k : int = 19

# Test pour Hyppodocus seul (à décommenter pour tester)
# cible = cible1
# voisins = knn_pokemon(dicos_pokemon, cible, k)
# types_voisins = frequence_des_types(voisins)
# type_cible = type_majoritaire(types_voisins)
# print(cible['nom'], 'est surement de type', type_cible)

print("Test des 5 cibles:")
for pokemon in [cible1, cible2, cible3, cible4, cible5]:
    cible = pokemon
    voisins = knn_pokemon(dicos_pokemon, cible, k)
    types_voisins = frequence_des_types(voisins)
    type_cible = type_majoritaire(types_voisins)
    print(cible['nom'], 'est surement de type', type_cible)
print("-" * 50)

## Pour tester les effets de diverses valeurs de k :
# for k in [1, 7, 30, 80]:
#     for pokemon in [cible1, cible2, cible3, cible4, cible5]:
#         cible = pokemon
#         voisins = knn_pokemon(dicos_pokemon, cible, k)
#         types_voisins = frequence_des_types(voisins)
#         type_cible = type_majoritaire(types_voisins)
#         print(cible['nom'], 'est surement de type', type_cible)
#     print()

# 27.
# Commentaires à la question 27.
rep_27 : str = """Après avoir testé les différentes formes de distances sur les 5 exemples de fin, on remarque que :
pour l'Euclidienne et celle de Manhattan, 3 des 5 prédictions sont les mêmes. En revanche la distance de Tchebychev 
donne des résultats complètements différents.
 
Pour k, après avoir testé différentes valeurs de k, les prédictions varient drastiquement en fonction de k.

Les résultats ne sont donc pas stables."""
print(rep_27, "\n" + "-" * 50)

# 28.
# Commentaires à la question 28.
rep_28 : str = """En regardant la représentation des types à l'ensemble de la table des pokemons, on remarque 
que certains types sont beaucoup plus représentés que d'autres, ainsi ils ont plus de chance d'être voisins des 
cibles et les 'favorise' alors dans le processus de prédiction (car ont "plus de chances" d'être voisins de la 
cible).
On en conclut alors qu'au vu de ces différences d'effectifs, les résultats sont largements discutables et la 
table peu efficace dans l'entraînement d'une intelligence artificielle."""
print(rep_28, "\n" + "-" * 50)

rep_28_comp : str = """Si on se base sur la table fournie par l'énoncé, le groupe le moins représenté (vol) ne 
comprends n'est représenté que par deux pokemons. Sur l'autre table fournie (+1000 pokemons), le nombre de pokemons 
possedant le type vol passe à 10, et 132 en comptant les doubles types.
A l'inverse, d'autres types se trouvent beaucoup plus représentés, commme Eau (59, 149, 172 dans les cas précédents),
rendant très discutable le jeu de données, qui semble largement favoriser les types plus représentés.

Pour une table de 400 Pokemons, la table semble alors bien trop faible pour entraîner une intelligence 
artificielle à deviner le type d'un Pokemon. Sur une table de 1000, les chiffres semblent encore faibles, 
cependant, les pokemons ayant un nombre limité de données disponibles, la nature même des objets d'étude limitent 
grandement les possibilités de données d'entraînement pour une intelligence artificielle.

Au vu des différences d'effectifs, les résultats sont alors très largement discutables et la 
table peu efficace dans l'entraînement d'une intelligence artificielle."""

print("Fin.", "\n" + "-" * 50)
### Fin.