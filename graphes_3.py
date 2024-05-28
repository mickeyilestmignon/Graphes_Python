from graphes_1 import *
from graphes_2 import *

auto3 ={"alphabet":['a','b'],"etats": [0,1,2,],
"transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

#3.1

def complet(A):
    
    for e in A["etats"]:
        dicoEtatsLettre = {lettre: False for lettre in A["alphabet"]}
        for t in A["transitions"]:
            if t[0] == e:
                dicoEtatsLettre[t[1]] = True # On met à True si il existe une transition partant de l'état avec la lettre
        for lettre in dicoEtatsLettre:
            if not dicoEtatsLettre[lettre]: # Si un est à False, ce n'est pas complet
                return False
    return True

#3.2

def complete(A):
    
    dicoEtatsLettre = dict();
    
    for e in A["etats"]:
        dicoEtatsLettre[e] = {lettre: False for lettre in A["alphabet"]}
        for t in A["transitions"]:
            if t[0] == e:
                dicoEtatsLettre[e][t[1]] = True
                
    etatPuit = len(A["etats"])
    
    ajoute = False
    for e in A["etats"]:
        for lettre in A["alphabet"]:
            if not dicoEtatsLettre[e][lettre]:
                A["transitions"].append([e, lettre, etatPuit]) # Si un etat n'a pas de transition par la lettre, on en ajoute une vers l'état puits
                ajoute = True
    
    if ajoute:
        A["etats"].append(etatPuit)
        for lettre in A["alphabet"]:
            A["transitions"].append([etatPuit, lettre, etatPuit])
    
    return A

#3.3

def complement(A):
    autoDeter = renommage(determinise(A))
    autoDeter = complete(autoDeter) # Ne pas compléter un automate déterminisé sans renommer les états
    
    etatsFinaux = autoDeter["F"].copy()
    autoDeter["F"] = []
    
    for e in autoDeter["etats"]:
        if e not in etatsFinaux:
            autoDeter["F"].append(e)
            
    return autoDeter

if __name__ == "__main__":
    print(complet(auto0))
    print(complete(auto0))
    print(complet(auto0))
    print(complement(auto3))