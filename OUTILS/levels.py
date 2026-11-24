import numpy as np

def inverse_lerp(start, maxLevel, currentLevel):
    """Return how far value is between start and end, as a fraction."""
    return (value - start) / (end - start)

def lerp(start, end, t):
    """Return the value t fraction of the way from start to end."""
    return start + (end - start) * t

def fetchLevel(XP):
    start:int = 50
    end:int = 10000
    maxLevel:int = 20
    t:float = inverse_lerp(1, maxLevel, currentLevel);
    requiredXP:float = round(lerp(start, end, t));


def fetchLevelXP(level):
    #XP needed for prev LVL - current LVL
    return None


    
def hasLeveledUp(gameState, earnedXP):
    currentLevel = gameState["level"]
    newLevel = fetchLevel(gameState["XP"])
    if newLevel > currentLevel:
        gameState["level"]=newLevel
        #gameState["skillPoints"]+= newLevel-currentLevel
        return f"You have leveled up! You are now at level {newLevel}"
    else:
        return f"You have gained {earnedXP}"

        
#asks for amount of XP and then returns 

