## Introduction

# 1.
from random import choices, shuffle

def pwd_generator(Alpha:int, alpha:int, digit:int, spe:int)->str:
    lettres = "abcdefghijklmnopqrstuvwxyz"
    Lettres = lettres.upper()
    chiffres = "0123456789"
    speciaux = "#@$%?_"

    pwd = choices(Lettres, k=Alpha)
    pwd += choices(lettres, k=alpha)
    pwd += choices(chiffres, k=digit)
    pwd += choices(speciaux, k=spe)
    shuffle(pwd)
    return "".join(pwd)

#print(pwd_generator(2,2,2,3))