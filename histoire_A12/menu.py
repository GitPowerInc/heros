from OUTILS.carte import creer_carte
from random import randint, random
from time import *

def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Greetings, adventurer. What may your name be? ")
    classe: list = ["Knight", "Wizard", "Archer"]
    gameState: dict = {
        "nom": nom,
        "classe": "",
        "level": 1,
        "XP": 0,
        "force": 1,
        "stamina": 0,
        "maxStamina": 0,
        "mana": 0,
        "maxMana": 0,
        "HP": 1,
        "inventory": [],
        "maxStorage": 3,
        "carte":creer_carte(),
        "position":(0,1,1)
    }

    print("Choisissez votre classe : ")
    print("1 - Mage   2 - Chevalier   3 - Archer")
    choixPossibles: list = ["1","2"]
    choix: int = "-1"
    while choix not in choixPossibles:
        choix = input("> ")
        if choix == "1":
            gameState["inventory"].append("Wooden Sword")
            gameState["force"] = 7
            gameState["HP"] = 20
            gameState["stamina"] = 10
            gameState["maxStamina"] = 10

        elif choix == "2":
            gameState["inventory"].append("Wooden Stick")
            gameState["force"] = 10
            gameState["HP"] = 12
            gameState["mana"]=10
            gameState["maxMana"]=10

        elif choix == "3":
            gameState["inventory"].append("Wooden Bow")
            gameState["force"] = 7
            gameState["HP"] = 20
            gameState["mana"]=6
            gameState["maxMana"]=6
            gameState["stamina"] = 8
            gameState["maxStamina"] = 8

        else:
            print("Choix invalide.")

    gameState["classe"] = classe[int(choix)-1]

    print(f"Bienvenue dans le donjon, honorable {gameState['classe']} ! Voici vos stats :")
    for nom, val in list(gameState.items())[2:]:
        print(f"\t- {nom.capitalize()}: {val}")
    return gameState
