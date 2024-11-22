#### Fonction secondaire
"""
Gautier BOUETEL 
Code qui peremt de verifier si un mot est un palindrome
"""


def ispalindrome(p):
    """
    Permet de veriier si un mot est un palindromes
    """
    table = str.maketrans("éèêëàâîïôùç", "eeeeaaiiouc", ",;:!?.§^¨€&'(-_)= ")
    p = p.lower()
    p = p.translate(table)
    m=len(p)-1
    i=0
    while i < m :
        if p[i]!=p[m]:
            return False
        i+=1
        m-=1
    return True

#### Fonction principale


def main():
    """
    appel de la fonction secondaire
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
