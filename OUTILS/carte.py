def creer_carte()->list:
    """Renvoie la carte, prédéfinie.
    Signification de chaque élément :
    d : départ
    f : fin
    . : salle vide
    m : salle avec des monstres
    p : salle avec un piège
    b : salle avec un boss
    T : salle contenant uniquement un trésor
    s : salle avec un secret
    a : salle avec un marché où l'on peut faire des achats
    majuscule : présence d'un trésor

    Returns:
        list: La carte, sous forme de liste.
    """
    res = [ # Ebauche
        [["d","m","T",".","m","m"],
         [".","M","m","p",".","P"],
         ["p","T",".","m",".","T"],
         ["m",".","p",".","M","p"],
         ["m","p","m","B","p","m"],
         ["T","M","a","f","m","s"]],
        [],
        []
    ]
    return res

def afficher_carte(etage:int)->None:
    """Affiche un étage de la carte avec des prints, ne renvoie rien.

    Args:
        etage (int): Le numéro de l'étage à afficher
    """    
    # à faire par LPDJ