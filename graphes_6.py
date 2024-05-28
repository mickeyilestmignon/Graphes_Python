from graphes_2 import *

auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],
"transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],
[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],
"I":[0],"F":[0,1,2,5]}

def dansQuelleClasse(classes, e):
    for i in range(len(classes)):
        if e in classes[i]:
            return i
    print("erreur")
    return False

def getClassTuple(classes, anciennesClasses, e):
    classList = list()
    for lettre in classes[e]:
        classList.append(dansQuelleClasse(anciennesClasses, classes[e][lettre]))
    return tuple(classList)

def tousMemesElements(T):
    """
    Renvoie true si tous les élements de la listes sont identiques, False sinon.
    """
    pass

def trouveNouvellesClasses(anciennesClasses, dicoEtatsLettre):
    nouvellesClasses = list()
    for classe in anciennesClasses:
        etatsPlaces = []
        for e in classe:
            newClasse = []
            classesEtat = getClassTuple(dicoEtatsLettre, anciennesClasses, e) # classes des etats par transition de e
            for e2 in classe:
                if classesEtat == getClassTuple(dicoEtatsLettre, anciennesClasses, e2) and e2 not in etatsPlaces: # tous ceux qui sont identiques dans la classe sont regroupés
                    newClasse.append(e2)
                    etatsPlaces.append(e2) # Pour ne pas qu'on l'ajoute plusieurs fois
        
            if newClasse: # Si la classe n'est pas vide
                nouvellesClasses.append(newClasse)
    
    return nouvellesClasses

def classes(A):
    """
    Trouve les classes minimales d'états pour l'automate A
    """
    # Tableau
    
    dicoEtatsLettre = dict();
    for e in A["etats"]:
        dicoEtatsLettre[e] = {lettre: [t[2] for t in A["transitions"] if t[0] == e and t[1] == lettre][0] for lettre in A["alphabet"]}
    
    # Niveau 0
    
    anciennesClasses = [[],A["F"]]
    for e in A["etats"]:
        if e not in A["F"]:
            anciennesClasses[0].append(e)
    
    # Niveau 1
    
    nouvellesClasses = trouveNouvellesClasses(anciennesClasses, dicoEtatsLettre)
    
    # Niveaux suivants, tant qu'ils ne sont pas identiques
                
    while anciennesClasses != nouvellesClasses:
        anciennesClasses = list(nouvellesClasses)
        nouvellesClasses = trouveNouvellesClasses(anciennesClasses, dicoEtatsLettre)
        
    return nouvellesClasses

def minimise(A):
    
    dicoEtatsLettre = dict(); # Tableau
    for e in A["etats"]:
        dicoEtatsLettre[e] = {lettre: [t[2] for t in A["transitions"] if t[0] == e and t[1] == lettre][0] for lettre in A["alphabet"]} # Les etats ne doivents pas êtres des listes, renommer avant de minimiser
    
    autoMini ={"alphabet":list(A["alphabet"]),"etats": classes(A), # Classes minimales
    "transitions":[],
    "I":[],"F":[]}
    
    print(autoMini["etats"])
    
    for e in autoMini["etats"]: # Transitions
        for lettre in autoMini["alphabet"]:
            transition = [e, lettre]
            for e2 in autoMini["etats"]:
                if dicoEtatsLettre[e[0]][lettre] in e2:
                    transition.append(e2)
            autoMini["transitions"].append(transition)
    
    for e in autoMini["etats"]: # Etats initiaux
        for etatInitial in A["I"]:
            if etatInitial in e and e not in autoMini["I"]:
                autoMini["I"].append(e)
                
    for e in autoMini["etats"]: # Etats finaux
        for etatInitial in A["F"]:
            if etatInitial in e and e not in autoMini["F"]:
                autoMini["F"].append(e)
    
    return autoMini

if __name__ == "__main__": # Les etats n'ont pas les memes nom a cause du renommage (ordre des etats dans la liste de l'automate)
#     print(minimise(auto6))
#     print(renommage(minimise(auto6)))
    
    b = {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4, 5, 6, 7], 'transitions': [[0, 'a', 1], [1, 'b', 1], [1, 'a', 3], [3, 'b', 3], [3, 'a', 5], [5, 'b', 1], [5, 'a', 6], [6, 'a', 7], [7, 'b', 7], [7, 'a', 6], [6, 'b', 2], [0, 'b', 2], [2, 'b', 2], [2, 'a', 4], [4, 'b', 4], [4, 'a', 2]], 'I': [0], 'F': [1, 3, 2, 6]}
    print("\n", minimise(b))
    print("\n", renommage(minimise(b)))