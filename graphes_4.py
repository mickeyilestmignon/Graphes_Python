from graphes_1 import *
from graphes_2 import *
from graphes_3 import *

auto4 ={"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}

auto5 ={"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
"I":[0],"F":[0,1]}

#4.1

def memeAlphabet(A1, A2):
    return set(A1["alphabet"]) == set(A2["alphabet"])

def inter(A1, A2):
    
    # Verifier que les alphabets sont identiques
    if not memeAlphabet(A1, A2):
        print("Les alphabets sont différents !")
        return
    
    # Renommage, aucun états n'ont le même nom
    A2 = renommage(A2, len(A1["etats"]))
    
    autoInter ={"alphabet":A1["alphabet"],
        "etats": [],
        "transitions":[],
        "I":[],
        "F":[]}
    
    etatInitial = [] # Construction de l'état initial
    for e in A1["I"]:
        etatInitial.append(e)
    for e in A2["I"]:
        etatInitial.append(e)
    autoInter["I"].append(etatInitial)
    
    produitRec(A1, A2, autoInter, etatInitial) # A la maniere de la determinisation
    
    for e in autoInter["etats"]: # Ajouter les etats finaux
        if e[0] in A1["F"] and e[1] in A2["F"]:
            autoInter["F"].append(e)
    
    return autoInter

def produitRec(A1, A2, autoInter, etatInitial):
    
    if etatInitial not in autoInter["etats"]:
            autoInter["etats"].append(etatInitial)
    
    for lettre in A1["alphabet"]:
        etatSuivant = []
        for e in etatInitial:
            for t in A1["transitions"]:
                if t[0] == e and t[1] == lettre:
                    if t[2] not in etatSuivant:
                        etatSuivant.append(t[2])
            for t in A2["transitions"]:
                if t[0] == e and t[1] == lettre:
                    if t[2] not in etatSuivant:
                        etatSuivant.append(t[2])
        
        if len(etatSuivant) >= 2:
            if [etatInitial, lettre, etatSuivant] not in autoInter["transitions"]:
                autoInter["transitions"].append([etatInitial, lettre, etatSuivant])
                produitRec(A1, A2, autoInter, etatSuivant)
                
#4.2

def difference(A1, A2):
    
    A1 = complete(A1)
    A2 = complete(A2)
    
    # Verifier que les alphabets sont identiques
    if not memeAlphabet(A1, A2):
        print("Les alphabets sont différents !")
        return
    
    # Renommage, aucun états n'ont le même nom
    A2 = renommage(A2, len(A1["etats"]))
    
    autoDiff ={"alphabet":A1["alphabet"],
        "etats": [],
        "transitions":[],
        "I":[],
        "F":[]}
    
    etatInitial = [] # Construction de l'état initial
    for e in A1["I"]:
        etatInitial.append(e)
    for e in A2["I"]:
        etatInitial.append(e)
    autoDiff["I"].append(etatInitial)
    
    produitRec(A1, A2, autoDiff, etatInitial)
    
    for e in autoDiff["etats"]: # Ajouter les etats finaux
        if e[0] in A1["F"] and e[1] not in A2["F"]:
            autoDiff["F"].append(e)
    
    return autoDiff

if __name__ == "__main__": # Les noms des états changent avec le renommage
#     print(inter(auto4, auto5), "\n")
#     print(renommage(inter(auto4, auto5)), "\n")
#     print(difference(auto4, auto5), "\n")
#     print(renommage(difference(auto4, auto5)))
    
    c = {'alphabet': ['a', 'b'], 'etats': [0, 1, 2], 'transitions': [[0, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 2]], 'I': [0], 'F': [2]}

    d = {'alphabet': ['a', 'b'], 'etats': [0, 1], 'transitions': [[0, 'a', 1], [1, 'a', 0], [0, 'b', 0], [1, 'b', 1]], 'I': [0], 'F': [0]}
    
    print("\n", inter(c, d))
    
    print("\n", renommage(inter(c, d)))