""""
@author: ntruong
"""

def Retourner(n:int)->int:
    """Retourne un nombre."""
    return int(str(n)[::-1])

def Est_un_palindrome(n:int)->bool:
    """Retourne si le nombre est un palindrome."""
    return n == Retourner(n)

def Palindromes(n:int)->int:
    """Retourne tous les palindromes inférieurs à n"""
    return [i for i in range(n + 1) if Est_un_palindrome(i)]

def ConstruitPalindrome(n:int, k:int)->int:
    """Construit un palindrome."""
    steps : int = 0
    while not Est_un_palindrome(n) and steps < k:
        n += Retourner(n)
        steps += 1
    return (n, steps) if Est_un_palindrome(n) else ("Pas de palindrome", steps)

## Tests:
print("Tests")
print("Q1)", Retourner(123))
print("Q2)", Est_un_palindrome(124))
print("Q3)", Palindromes(121))
print("Q4, 5, 6)", ConstruitPalindrome(12, 100))