def prefixe(A):
    autoPref ={"alphabet": list(A["alphabet"]), "etats": list(A["etats"]), "transitions": list(A["transitions"]), "I": list(A["I"]), "F": list(A["etats"])}
    return autoPref

def suffixe(A):
    autoSuff ={"alphabet": list(A["alphabet"]),"etats": list(A["etats"]),"transitions": list(A["transitions"]),"I": list(A["etats"]),"F": list(A["F"])}
    return autoSuff
                
def facteur(A):
    autoFact ={"alphabet": list(A["alphabet"]),"etats": list(A["etats"]),"transitions": list(A["transitions"]),"I": list(A["etats"]),"F": list(A["etats"])}
    return autoFact

def miroir(A):
    autoMiroir ={"alphabet": list(A["alphabet"]),"etats": list(A["etats"]),"transitions": [t[::-1] for t in A["transitions"]],"I": list(A["F"]),"F": list(A["I"])}
    return autoMiroir
    
if __name__ == "__main__":
    
    auto27 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 4], [1, 'b', 2], [2, 'a', 3], [2, 'b', 4], [3, 'a', 3], [3, 'b', 3], [4, 'a', 4], [4, 'b', 4]],
    "I": [1],
    "F": [4]
    }
    
    print(prefixe(auto27))
    print(suffixe(auto27))
    print(facteur(auto27))
    print(miroir(auto27))