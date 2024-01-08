"""
@author: ntruong
"""
from random import sample
from scipy.special import comb

valeurs=["7","8","9","10","V","D","R","A"]
couleurs=["T","K","C","P"]

# 1)
deck = [[v, c] for c in couleurs for v in valeurs]

# 2)
def tirerMain()->list:
    return sample(deck, 5)

# 3)
def estCouleur(main:list)->bool:
    # return all(c[1] == main[0][1] for c in main) # méthode avec all()
    return len(set([c[1] for c in main])) == 1 # méthode avec set()

# 4)
def estQuinte(main:list)->bool:
    return sorted([c[0] for c in main]) in [sorted(valeurs[i:i+5]) for i in range(0, 4)]

# 5)
tirages = 50_000

n_c, n_q, n_cq = 0, 0, 0
for i in range(tirages):
    main = tirerMain()
    if estCouleur(main):
        n_c += 1
        if estQuinte(main):
            n_cq += 1
    elif estQuinte(main):
        n_q += 1

print("Probabilité d'obtenir une couleur :", 100 * n_c / tirages)
print("Probabilité d'obtenir une quinte :", 100 * n_q / tirages)
print("Probabilité d'obtenir une quinte floche :", 100 * n_cq / tirages)
print()

# 6)
nb_poss = comb(32, 5)

p_c_c = 100 * 4 * comb(8, 5) / nb_poss
print("Probabilité calculée d'obtenir une couleur :", p_c_c)

nb_quint = 4 ** 6
p_q_c = 100 * nb_quint / nb_poss
print("Probabilité calculée d'obtenir une quinte :", p_q_c)

nb_quint_floche = 4 * len([sorted(valeurs[i:i+5]) for i in range(0, 4)])
p_cq_c = 100 * nb_quint_floche / nb_poss
print("Probabilité calculée d'obtenir une quinte floche :", p_cq_c)

### Tests

# print(deck)
# print(len(deck) == 32)

# print(tirerMain())

m1 = [['9', 'C'], ['V', 'K'], ['10', 'C'], ['7', 'T'], ['7', 'C']]   # cette main n'est pas une couleur
m2 = [['9', 'C'], ['V', 'C'], ['10', 'C'], ['7', 'C'], ['7', 'C']]  # cette main est une couleur
m3 = [['D', 'C'], ['R', 'K'], ['A', 'C'], ['10', 'T'], ['V', 'C']]  # cette main est une Quinte
m4 = [['D', 'C'], ['R', 'C'], ['A', 'C'], ['10', 'C'], ['V', 'C']]  # cette main est une Quinte floche

# print(estCouleur(m2))
# print(estQuinte(m4))