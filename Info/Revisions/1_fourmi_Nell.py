"""
@author: ntruong
"""
from random import *
import matplotlib.pyplot as plt

## Question 1
def avancer()->list:
    return [[1,0], [0, -1], [0, 1], [-1, 0]][randint(0, 3)]

## Question 2
# fourmi = [0, 0]
# f_pos = [fourmi]
# while abs(fourmi[0]) <= 2 and abs(fourmi[1]) <= 2:
#     deplacement = avancer()
#     fourmi = [fourmi[i] + deplacement[i] for i in [0, 1]]
#     f_pos.append(fourmi)
# print(f_pos)

## Question 3
def traj(a:int):
    fourmi = [0, 0]
    f_pos = [fourmi]
    while abs(fourmi[0]) <= a and abs(fourmi[1]) <= a:
        deplacement = avancer()
        fourmi = [fourmi[i] + deplacement[i] for i in [0, 1]]
        f_pos.append(fourmi)
    return f_pos[:-1]

## Question 4
for i in range(6):
    t = traj(10)
    plt.plot([t[_][0] for _ in range(len(t))], [t[_][1] for _ in range(len(t))])
plt.show()

## Question 5
def LM(a:int, N:int)->float:
    """Renvoie la moyenne des longueurs des trajets de N fourmis dans une grille de taille a*a"""
    trajets = [len(traj(a)) for i in range(N)]
    return sum(trajets) / len(trajets)

## Question 6
# L_a = [LM(i, 1) for i in range(1, 21)]
# print(sum(L_a) / len(L_a))

## Tests:
# print(avancer())
# print(traj(2))
# print(LM(10, 6))