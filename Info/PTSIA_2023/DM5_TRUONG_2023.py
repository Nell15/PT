# @author: ntruong
# @title: DM5_TRUONG_2023

print("-" * 50)
print("DM5_TRUONG_2023.py")
print("-" * 50)

### Partie 1: Quelques Préliminaires

alphabet = "abcdefghijklmnopqrstuvwxyz"

def nettoyage(phrase:str)->str:
    """Nettoie une phrase de ses caractères spéciaux et la passe ne minuscule."""
    return "".join([lettre for lettre in phrase.lower() if lettre in alphabet])

def comptage(phrase:str)->dict:
    """Compte les occurences de chaques lettres dans une phrase."""
    d : dict = {l:0 for l in alphabet}
    for lettre in phrase:
        d[lettre] += 1
    return d

def frequence(phrase:str)->dict:
    """Retourne la fréquence des lettres d'une phrase."""
    n : int = len(phrase)
    compte : dict = comptage(phrase)
    return({l:compte[l] * 100 / n for l in alphabet})

def chi_deux(dico:dict, ref:dict):
    """Retourne la distance linguistique d'un texte à une langue 
    d'après la méthode la méthodes des moindres carrés."""
    return sum([((dico[lettre] - ref[lettre]) ** 2) / ref[lettre] for lettre in alphabet])

# Dictionnaire de référence des fréquences d'apparitions des lettres dans la langue anglaise.
ref = {'a':8.17,'b':1.49,'c':2.78,'d':4.25,'e':12.7,'f':2.23,'g':2.01,'h':6.10,
       'i':6.97,'j':0.15,'k':0.77,'l':4.03,'m':2.41,'n':6.75,'o':7.51,'p':1.93,
       'q':0.10,'r':5.99,'s':6.33,'t':9.06,'u':2.76,'v':0.98,'w':2.36,'x':0.15,
       'y':1.97,'z':0.07}

### Partie 2: Code César:

def decalage(n:int, lettre:str)->str:
    """Décale une lettre d'un nombre n."""
    return alphabet[(alphabet.index(lettre) + n) % 26]

def codage(n:str, phrase:str)->str:
    """Chiffre une phrase suivant le code César."""
    return "".join([decalage(n, lettre) for lettre in phrase])

def trouve_decalage(phrase:str)->int:
    """Trouve la valeur probable du décalage d'un code chiffré 
    par code César."""
    stock : dict = {n:chi_deux(frequence(codage(n, phrase)), ref) for n in range(0, 25)}
    n_probable : int = min(stock, key=stock.get)
    return 26 - n_probable

def decodage(phrase:str)->str:
    """Décode une phrase chiffrée par code César."""
    return codage(-trouve_decalage(phrase), phrase)

### Partie 3: le chiffre de Vigenère:

def code_Vigenere(phrase:str, cle:str)->str:
    """Chiffre une phrase par chiffrement de Vigenère."""
    return "".join([decalage(alphabet.index(cle[i % len(cle)]), phrase[i]) for i in range(len(phrase))])


def decode_Vigenere(phrase:str, cle:str)->str:
        return "".join([decalage(-alphabet.index(cle[i % len(cle)]), phrase[i]) for i in range(len(phrase))])

def IC(phrase:str)->float:
    occurences : dict = comptage(phrase)
    n : int = len(phrase)
    return 26 * sum([occurences[lettre] * (occurences[lettre] - 1) for lettre in alphabet]) / (n * (n - 1))

def bonus(texte:str)->str:
    with open(texte, encoding = 'utf-8') as f:
        data = f.read()
        phrase, L = [], []

        # Découpe du texte:
        for k in range(1, 13):
            n = len(data) // k
            L_t = [data[i:n+1:k] for i in range(k)]
            phrase.append(L_t)

        # Recherche de l'IC:
        for L_t in phrase:
            moy = sum([IC(t_k) for t_k in L_t]) / len(L_t)
            L.append(moy)
        k = L.index(max(L)) + 1

        # Recherche de la clé:
        cle = ''
        t_k = [data[i:n + 1:k] for i in range(k)]
        for sous_t in t_k:
            n = trouve_decalage(sous_t)
            cle += alphabet[n]

        # On a le texte chiffré et on a trouvé la clé
        # On retourne le texte décodé:
        return decode_Vigenere(data, cle)


### Tests et réponses:

phrase = "Que J'aime à faire le DM d'Informatique !"
net = nettoyage(phrase)
reponse_1 = f"La phrase nettoyée est : {net}"

occ = comptage(net)
reponse_2 = f"Occurences des lettres dans cette phrase:{occ}"

freq = frequence(net)
reponse_3 = f"On en déduit la fréquence d'utilisation des lettres : {freq}"

phrase_2 = "computer"
dico = frequence(phrase_2)
chi_2 = chi_deux(dico, ref)
reponse_4 = f"La distance de la phrase à la langue de référence (ici l'Anglais) est de {chi_2}"

a_d = decalage(3, "a")
z_d = decalage(3, "z")
reponse_5 = f"""Un décalage de 3 pour a donne {a_d} et pour z donne {z_d}"""

c_cesar = codage(3, "computer")
reponse_6 = f"Le mot {phrase_2} une fois chiffré devient {c_cesar}"

reponse_7: str = """On peut bruteforce le problème et tester les 25 
possibilités non triviales de décalage afin de trouver la bonne valeur de 
celui-ci et donc la phrase. Par ailleurs, pour ne pas avoir à vérifier 
manuellement les 25 possibilités, on peut faire une analyse fréquentielle 
des lettres dans le texte et comparer la fréquences des lettres à celle de 
la langue supposée du texte."""

dec = trouve_decalage("frpsxwhu")
reponse_8 = f"Le mot {c_cesar} provient supposément d'un décalage de {dec} lettres."

deco = decodage("frpsxwhu")
reponse_9 = f"Le mot frpsxwhu une fois décodé redevient: {deco}."

code_V = code_Vigenere("anticonstitutionnellement", "roue")
reponse_10 = f"Le mot 'anticonstitutionnellement' une fois chiffré par Vigenère donne '{code_V}'."

reponse_11 = """L'intérêt d'un code Vigenère est d'être beaucoup plus complexe 
à décrypter qu'un code César. Il est donc plus sécurisé."""

deco_V = decode_Vigenere("rbnmtchwkwnykwiresfpvayrk", "roue")
reponse_12 = reponse_10 = f"Le mot 'rbnmtchwkwnykwiresfpvayrk' une fois chiffré par Vigenère donne '{deco_V}'."

ic = IC("anticonstitutionnellement")
reponse_13 = f"L'indice de coincidence de 'anticonstitutionnellement' est {ic}."

bon = bonus("DM5_texte_code.txt")
reponse_14 = f"Le texte une fois décrypté se traduit par : \n{bon}"

liste_reponses = [reponse_1, reponse_2, reponse_3, reponse_4, reponse_5, 
                  reponse_6, reponse_7, reponse_8, reponse_9, reponse_10, 
                  reponse_11, reponse_12, reponse_13, reponse_14]

for X in range(1, 15):
    print(f"Question {X}:")
    print(liste_reponses[X - 1])
    print("-" * 50)

print("FIN")
print("-" * 50)