from random import sample


def shop(i:int)->None:
    """Manages the shops.

    Args:
        i (int): The index of the shop.
    """    
# Combinaisons, listes d'items
    name=["John","Michel"]
    items=[
        ["arrows","health potion", "silver armor","blablabla"],
        []
        ]
    
    print ("Hello, welcome to {name[i]}'s shop! What would you like to buy today.")