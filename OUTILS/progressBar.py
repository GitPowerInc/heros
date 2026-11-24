# health, xp, hunger, stamina, mp

#[+++++++++------] (red, blue, purple etc)

def bar(typ, gameState):
    color=""
    length=15
    stat=gameState[typ]
    maxStat=gameState["max"+typ.capitalize()]
    nb_plus=round(stat/maxStat*length)
    nb_minus=length-nb_plus
    if typ=="health":
        color="#1253FF"
    bar="[" + "+"*nb_plus + "-"*nb_minus + "]"
        #for i in range():

    return bar






    

