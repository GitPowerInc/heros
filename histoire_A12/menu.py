def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Quel est votre nom ? ")
    classe: list = ["Mage, Chevalier, TBD"]

    gameState: dict = {
        "nom": nom,
        "force": 1,
        "vie": 1,
        "inventaire": [],
    }

    print("Choisissez votre classe : ")
    print("1 - Mage   2 - Chevalier   3 - TBD")
    choix: str = input("> ")
    if choix == "1":
        gameState["inventaire"].append("Wooden Sword")
        gameState["force"] = gameState["force"] + 3
        print(f"Votre force passe à {gameState['force']}.")
        res = 2
    elif choix == "2":
        res = 2
    else:
        print("Choix invalide.")
        res = 1                  # on reste sur cette page


    print(f"Bienvenue, {nom} ! Force : {gameState['force']}, Vie : {gameState['vie']}\n")
    return gameState
