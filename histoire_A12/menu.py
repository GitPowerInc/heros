def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Quel est votre nom ? ")
    classe: list = ["Mage", "Chevalier", "TBD"]
    gameState: dict = {
        "nom": nom,
        "force": 1,
        "classe": "",
        "HP": 1,
        "inventaire": [],
        "maxStorage": 3,
        "XP": 0,
        "LVL": 1
    }

    print("Choisissez votre classe : ")
    print("1 - Mage   2 - Chevalier   3 - TBD")
    choixPossibles: list = ["1","2"]
    choix: int = "-1"
    while choix not in choixPossibles:
        choix = input("> ")
        if choix == "1":
            gameState["inventaire"].append("Wooden Stick")
            gameState["force"] = 10
            gameState["HP"] = 12
        elif choix == "2":
            gameState["inventaire"].append("Wooden Sword")
            gameState["force"] = 7
            gameState["HP"] = 20
        else:
            print("Choix invalide.")

    gameState["classe"] = classe[int(choix)-1]

    print(f"Bienvenue dans le donjon, honorable {gameState['classe']} ! Voici vos stats : \n\t - Force : {gameState['force']} \n\t - HP : {gameState['HP']}\n")
    return gameState
