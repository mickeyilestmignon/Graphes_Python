from graphes_1 import *

auto0 ={"alphabet":['a','b'],
        "etats": [0,1,2,3],
        "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]],
        "I":[0],
        "F":[3]}

auto1 ={"alphabet":['a','b'],
        "etats": [0,1],
        "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]],
        "I":[0],
        "F":[1]}

auto2={"alphabet":['a','b'],
       "etats": [0,1],
        "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]],
       "I":[0],
       "F":[1]}

autoTest={"alphabet":['a','b'],
       "etats": [0,1,2,3],
        "transitions":[[0,'a',0], [0,'a',1], [0,'b',0], [0,'b',3], [0,'b',1], [1,'a',0], [1,'b',2], [3,'b',3], [3,'b',1]],
       "I":[0, 1],
       "F":[2]}

#2.1

def neutralLetterDict(A):
    dicoLettres = dict()
    for lettre in A["alphabet"]:
        dicoLettres[lettre] = False
    return dicoLettres

def deterministe(A):
    if len(A["I"]) > 1:
        return False
    for e in A["etats"]:
        dicoLettres = neutralLetterDict(A)
        for t in A["transitions"]:
            if t[0] == e:
                if not dicoLettres[t[1]]:
                    dicoLettres[t[1]] = True
                else:
                    return False
    return True

#2.2

def determinise(A):
    autoDeter ={"alphabet":A["alphabet"],
        "etats": [],
        "transitions":[],
        "I":[],
        "F":[]}
    
    etatInitial = [] # Construction de l'état initial
    for e in A["I"]:
        etatInitial.append(e)
    autoDeter["I"].append(etatInitial)
    
    determiniseRec(A, autoDeter, etatInitial)
    
    return autoDeter
    
def determiniseRec(A, autoDeter, etatInitial):
    if etatInitial not in autoDeter["etats"]: # L'ajouter si il n'y est pas
            autoDeter["etats"].append(etatInitial)
    
    for lettre in A["F"]: # Si l'état doit être final
        if lettre in etatInitial:
            if etatInitial not in autoDeter["F"]:
                autoDeter["F"].append(etatInitial)
    
    for lettre in A["alphabet"]:
        etatSuivant = []
        for e in etatInitial:
            for t in A["transitions"]:
                if t[0] == e and t[1] == lettre:
                    if t[2] not in etatSuivant:
                        etatSuivant.append(t[2])
        
        if etatSuivant:
            if [etatInitial, lettre, etatSuivant] not in autoDeter["transitions"]:
                autoDeter["transitions"].append([etatInitial, lettre, etatSuivant])
                determiniseRec(A, autoDeter, etatSuivant)

#2.3

def renommage(A, offset=0):
    dicoRenommage = dict()
    for i in range(len(A["etats"])):
        dicoRenommage[str(A["etats"][i])] = i + offset # Renommer les etats par noms croissants à partir de offset
        A["etats"][i] = dicoRenommage[str(A["etats"][i])]
        
    for i in range(len(A["I"])):
        A["I"][i] = dicoRenommage[str(A["I"][i])]
    
    for i in range(len(A["F"])):
        A["F"][i] = dicoRenommage[str(A["F"][i])]
        
    for i in range(len(A["transitions"])):
        A["transitions"][i][0] = dicoRenommage[str(A["transitions"][i][0])]
        A["transitions"][i][2] = dicoRenommage[str(A["transitions"][i][2])]
    
    return A

if __name__ == "__main__":
#     print(deterministe(auto0))
#     print(deterministe(auto2))
#     print(determinise(auto2))
#     print(renommage(determinise(auto2)))
    
    a = {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3], 'transitions': [[0, 'a', 1], [1, 'a', 2], [2, 'a', 0], [1, 'a', 0], [0, 'b', 3], [3, 'b', 0]], 'I': [0, 3], 'F': [0]}
    print("\n", determinise(a))
    print("\n", renommage(determinise(a)))