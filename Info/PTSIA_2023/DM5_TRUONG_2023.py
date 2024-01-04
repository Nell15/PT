# @author: ntruong
# @title: DM5_TRUONG_2023

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

# Récupéré chez mon fisto, à vérifier que c'était dans le sujets
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
    N, S = len(phrase), 0
    dico = comptage(phrase)
    for lettre in dico:
        S += dico[lettre] * (dico[lettre] - 1)
    IC = (26 / (N * (N-1))) * S
    return IC

def bonus(texte:str)->str:
    
    with open(texte, encoding = 'utf-8') as f:
        data = f.read()
        phrase, L = [], []

        # Découpe du texte
        for k in range(1, 13):
            n = len(data) // k
            L_t = [data[i:n+1:k] for i in range(k)]
            phrase.append(L_t)

        # Recherche de l'IC
        for L_t in phrase:
            moy = sum([IC(t_k) for t_k in L_t]) / len(L_t)
            L.append(moy)
        k = L.index(max(L)) + 1

        # Recherche de la clé
        cle = ''
        t_k = [data[i:n + 1:k] for i in range(k)]
        for sous_t in t_k:
            n = trouve_decalage(sous_t)
            cle += alphabet[n]

        texte_deco = decode_Vigenere(data, cle)
        return texte_deco

### Tests:

net = nettoyage("Que J'aime à faire le DM d'Informatique !")
reponse_1 = f"La phrase nettoyée est : {net}"

reponse_2 = frequence("quejaimefaireledmdinformatique")

phrase = "computer"
dico = frequence(phrase)
reponse_3 = chi_deux(dico, ref)

print(decalage(3, "a"))
print(decalage(3, "z"))

# print(codage(3, "computer"))

reponse_7: str = """On peut bruteforce le problème et tester les 25 
possibilités non triviales de décalage afin de trouver la bonne valeur de 
celui-ci et donc la phrase. Par ailleurs, pour ne pas avoir à vérifier 
manuellement les 25 possibilités, on peut faire une analyse fréquentielle 
des lettres dans le texte et comparer la fréquences des lettres à celle de 
la langue supposée du texte."""

# print(reponse_7)

# print(trouve_decalage("frpsxwhu")) # = 3 si tout marche

# print(decodage("frpsxwhu"))

# reponse_10 = 'a_faire'

reponse_11 = """L'intérêt d'un code Vigenère est d'être beaucoup plus complexe 
à décrypter qu'un code César. Il est donc plus sécurisé."""

print("Bonus :", bonus("DM5_texte_code.txt"))