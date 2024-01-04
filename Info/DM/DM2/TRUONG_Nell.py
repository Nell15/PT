"""
DM SQL PT 2021
@author: TRUONG - Nell
"""

import sqlite3
bdr = sqlite3.connect('./carte.sqlite') # connexion Ã  la base de donnÃ©e 
cur = bdr.cursor()
import matplotlib.pyplot as plt

def requete(commande): # pour gagner en lisibilitÃ©, appeler la fonction requÃªtes dans le shell
	cur.execute(commande)
	result = cur.fetchall()
	print(result)

## Introduction

# 1.
commande1 = """SELECT a.nom, b.nom FROM 'communes' a
    JOIN 'depts' b ON a.dep_id = b.id
ORDER BY superficie DESC LIMIT 0,10"""
# requete(commande1)
# ARLES
# SAINTES-MARIES-DE-LA-MER
# LARUNS
# CHAMONIX-MONT-BLANC
# SAINT-CHRISTOPHE-EN-OISANS
# HOURTIN
# LACANAU
# SAINT-MARTIN-DE-CRAU
# SAINT-PAUL-SUR-UBAYE
# SARTENE

# 2.
commande2 = """SELECT a.nom, MAX(altitude), b.nom FROM (SELECT * FROM 'communes' WHERE population > 10) a
    JOIN 'depts' b ON a.dep_id = b.id"""
# requete(commande2)
# BRIANCON / 1586 / HAUTES-ALPES

# 3.
commande3 = """SELECT c.nom 
FROM 'communes' c
    JOIN (SELECT a.dep_id, MIN(pop_totale), chef_lieu
        FROM (SELECT dep_id, SUM(population) AS pop_totale FROM 'communes' GROUP BY dep_id) a
            JOIN 'depts' b ON a.dep_id = b.id) d ON c.id = d.chef_lieu"""
# requete(commande3)
# Mende (18292)
# Note: c'est celui de la Lozère

# 4.
commande4 = "SELECT AVG(superficie) FROM 'communes' WHERE dep_id IN (SELECT id FROM 'depts' WHERE code == '2A' OR code == '2B')"
# requete(commande4)
# Superficie moyenne des commmunes en Corse : 2432.777777777778 Hectares

# 5.
commande5 = "SELECT AVG(s_sum) FROM (SELECT dep_id, SUM(superficie) AS s_sum FROM 'communes' GROUP BY dep_id)"
# requete(commande5)
# superficie moyenne des départements métropolitains : 571173.6458333334 Hectares

# 6.
commande6 = """SELECT b.nom, MAX(s_sum)
FROM (SELECT dep_id, SUM(superficie) AS s_sum FROM 'communes' GROUP BY dep_id) a
    JOIN 'depts' b ON a.dep_id = b.id"""
# Le département au plus vastes communes est le Gironde
# requete(commande6)

# 7.
commande7 = """SELECT a.nom, b.nom
FROM (SELECT nom, dep_id, MIN(10*population/superficie) AS min_densite FROM 'communes' WHERE population > 1) a
    JOIN 'depts' b ON a.dep_id = b.id"""
# requete(commande7)
# La commune de plus faible densité est LARUNS en PYRENEES-ATLANTIQUES

# 8.
commande8 = """SELECT ta1.nom, ta1.altitude, ta1.superficie, ta1.dep_id
FROM 'communes' ta1
JOIN 'communes' ta2 on ta1.id != ta2.id
WHERE ta1.superficie = ta2.superficie and ta1.altitude = ta2.altitude and ta1.dep_id = (SELECT id FROM 'depts' WHERE code == 62) and ta2.dep_id = (SELECT id FROM 'depts' WHERE code == 62)"""
# requete(commande8)
# Minfestement il y en a

# 9.
commande9 = """SELECT postal, MAX(p_count) FROM (
SELECT *, count(postal) AS p_count
FROM 'communes'
GROUP BY postal)"""
# requete(commande9)
# Le code postal est : 51300
# et est utilisé 46 fois

## Interaction de Python avec la base de donnÃ©es

# 10.
def chef_lieu(s):
	chefLieu = f"SELECT nom FROM 'communes' WHERE id = (SELECT chef_Lieu FROM 'depts' WHERE code = '{s}')"
	cur.execute(chefLieu)
	return cur.fetchall()

# TEST :
# On va tenter de vérifier que le chef lieu de la Lozère (48)
# print(chef_lieu(48))

# 11.
def prefecture(s):
	pref = []
	chefs = f"SELECT chef_lieu FROM 'depts' WHERE id IN (SELECT dep_id FROM 'communes' WHERE nom = '{s}')"
	cur.execute(chefs)
	res = cur.fetchall()
	for i in range(len(res)):
		n = res[i][0]
		req_nom = f"SELECT nom FROM 'communes' WHERE id = {n}"
		cur.execute(req_nom)
		res1 = cur.fetchall()
		pref.append(res1[0][0])
	return pref

# TEST
# print(prefecture('SAINTE-COLOMBE'))
# print("Pour la ville de Sainte-Colombe, il y a", len(prefecture('SAINTE-COLOMBE')), "réponses.")

# 12.
def code_postal_inverse(n):
	req = f"""SELECT a.nom, b.nom
			FROM (SELECT * FROM 'communes' WHERE postal LIKE '%{n}%') a
    			JOIN 'depts' b ON a.dep_id = b.id"""
	cur.execute(req)
	res = cur.fetchall()
	departement, communes = [], []
	for couple_act in res:
		comm_act, dep_act = couple_act
		if dep_act not in departement: departement.append(dep_act)
		communes.append(comm_act)
	return None if len(departement) == 0 else (departement[0], communes)

# TESTS
# print(code_postal_inverse(42440)) # On s'attends à plusieurs résultats
# print(code_postal_inverse("01280")) # On s'attends à un seul résultat
# print(code_postal_inverse(19075124305987))  # On s'attends à aucun résultats

# 13.

# Inclue dans la question 12

# 14.

data = []
for i in range(5):
	data.append(0) # Pour modifier data sans toucher à la "ligne 1" ;)
# Note les valeurs dans data vont correspondre aux nombre de commmunes dans les tranches d'altitude
# Les tranches d'altitudes sont notées dans data dans le même ordre que dans label

# On effectue une requete pour obtenir les altitudes des communes
cur.execute("SELECT altitude FROM 'communes'")
alt_req = cur.fetchall()

# Pour chaque commmune, on ajoute 1 à la tranche d'altitude à laquelle elle corresponds dans data (le camembert)
for i in range(len(alt_req)):
	alt_act = alt_req[i][0]
	if alt_act < 50:
		data[0] += 1
	elif 50 <= alt_act < 100:
		data[1] += 1
	elif 100 <= alt_act < 500:
		data[2] += 1
	elif 500 <= alt_act < 1000:
		data[3] += 1
	else :
		data[4] += 1

label = ['-50', '50-100', '100-500', '500-1000', '1000+']
plt.title("Nombre de communes par tranches d'altitude", fontdict=None, loc='center')
plt.pie(data, explode=(0, 0, 0.1, 0, 0), labels=label, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.show()

## TracÃ© de contours

# 15.
def polygone(c, i):
	cur.execute("SELECT p.x, p.y FROM pointsdep p JOIN depts d ON p.iddept = d.id WHERE d.code='{}' and p.poly={} ORDER BY p.ordre ASC".format(c, i))
	result = cur.fetchall()
	return [r[0] for r in result], [r[1] for r in result]

# La fonction polygône retourne la position (absisses et ordonnée) de chacun des points à coloriers pour former le département
# La fonction crée un tableau de ces valeurs à partir d'une jointure entre les tables : pointsdep et depts
# La table depts sert à associer le département souhaité à un indice qui permet de repérer les points à colorier, donnés dans pointsdeps

# 16.
def dessine_departement(c, couleur='blue'):
	cur.execute("SELECT DISTINCT poly FROM pointsdep p JOIN depts d ON p.iddept = d.id WHERE d.code='{}'".format(c))
	poly = [r[0] for r in cur.fetchall()]
	for i in poly:
		x, y = polygone(c, i)
		plt.fill(x, y, color=couleur)

# La fonction dessine departement trace le point par point le département donné en entrée
# La requete SQL retourne le type de polygône necessaire au tracé du département
# Par la suite on rempli tous les points associés au département et type de polygône grâce à la fonction précédente

# 17.

plt.axes().set_aspect(1.5)			# Pour se conformer à l'aspect habituel
plt.title("Représentation de l'alsace", fontdict=None, loc='center')
dessine_departement(67, 'red')		# Trace le Bas-Rhin en rouge (couleur arbitrairement choisie) 
dessine_departement(68, 'blue')		# Trace le Haut-Rhin en bleu (couleur arbitrairement choisie) 
plt.show()

# 18.

# On récupère une liste de la forme suivante : [(poptotale du departement, code du département), (...), ...]
cur.execute("""SELECT a.s_pop, b.code
FROM (SELECT SUM(population) AS s_pop, dep_id FROM 'communes' GROUP BY dep_id) a
    JOIN 'depts' b ON a.dep_id = b.id""")
req = cur.fetchall()

# On cherche la population max pour le calcul de la proportionalité
cur.execute("""SELECT MAX(s_pop)
FROM (SELECT SUM(population) AS s_pop, dep_id FROM 'communes' GROUP BY dep_id) a
    JOIN 'depts' b ON a.dep_id = b.id""")
max_pop = cur.fetchall()[0][0]

plt.clf()
for i in range(len(req)):
	# On calcule un coefficient de proportionalité
	prop = req[i][0] / max_pop
	code = req[i][1]
	# Puis on dessine le département actuellement regardé
	# Ici j'ai arbitrairement choisi que la proportionalité se ferait sur la couleur rouge.
	dessine_departement(code, (prop, 0, 0))

titre = "Représentation de la France aux départements\n coloriés proportionellement à leur population"
plt.title(titre, fontdict=None, loc='center')
plt.show()
