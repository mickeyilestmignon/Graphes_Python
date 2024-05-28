auto ={"alphabet":['a','b'],
       "etats": [1,2,3,4],
       "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]],
       "I":[1],
       "F":[4]}

#1.1.1

def pref(u):
    """
    Renvoie la liste des préfixes de u.
    """
    prefixes = set()
    for i in range(len(u)+1):
        prefixes.add(u[:i])
    return list(prefixes)

#1.1.2

def suf(u):
    """
    Renvoie la liste des suffixes de u.
    """
    suffixes = set()
    for i in range(len(u)+1):
        suffixes.add(u[i:])
    return list(suffixes)

#1.1.3

def fact(u):
    facteurs = set()
    for i in range(len(u)+1):
        for j in range(i, len(u)+1):
            facteurs.add(u[i:j])
    return list(facteurs)

#1.1.4
def miroir(mot):
    return mot[::-1]

#1.2.1

def concatene(L1, L2):
    listConcat = set()
    for mot1 in L1:
        for mot2 in L2:
            listConcat.add(mot1 + mot2)
    return list(listConcat)

L1=['aa','ab','ba','bb']
L2=['a', 'b', '']

#1.2.2

def puisRec(L1, L2, n, i):
    if i < n:
        return puisRec(concatene(L1, L2), L2, n, i + 1)
    return L1

def puis(L, n):
    return puisRec(L, L, n, 1)

L3=['aa','ab','ba','bb']

#1.2.3 - Car la mémoire est limitée.

#1.2.4

def tousmotsRec(A, n, mots):
    if n == 0:
        return list(mots)
    else:
        nouveaux_mots = mots.copy()
        for lettre in A:
            for mot in mots:
                nouveaux_mots.add(mot + lettre)
        return tousmotsRec(A, n-1, nouveaux_mots)

def tousmots(A, n):
    mots = set()
    mots.add('')
    return tousmotsRec(A, n, mots)

#1.3.1

def defauto():
    auto ={"alphabet":[], "etats": [], "transitions":[], "I":[], "F":[]}
    
    s = input("Saisisez l'alphabet ['/' pour passer aux états] : ")
    while(s != "/"):
        auto["alphabet"].append(s)
        s = input("Saisisez l'alphabet ['/' pour passer aux états] : ")
    
    s = input("Saisisez les états ['/' pour passer aux transitions] : ")
    while(s != "/"):
        auto["etats"].append(int(s))
        s = input("Saisisez les états ['/' pour passer aux transitions] : ")
    
    t = []
    s = input("Saisisez les transitions, de la forme '[état initial] [lettre] [état final]' ['/' pour passer aux états initiaux] : ")
    while(s != "/"):
        s = s.split(" ")
        s[0] = int(s[0])
        s[2] = int(s[2])
        auto["transitions"].append(s)
        s = input("Saisisez les transitions, de la forme '[état initial] [lettre] [état final]' ['/' pour passer aux états initiaux] : ")
    
    s = input("Saisisez les états initiaux ['/' pour passer aux états finaux] : ")
    while(s != "/"):
        auto["I"].append(int(s))
        s = input("Saisisez les états initiaux ['/' pour passer aux états finaux] : ")
        
    s = input("Saisisez les états finaux ['/' pour terminer] : ")
    while(s != "/"):
        auto["F"].append(int(s))
        s = input("Saisisez les états finaux ['/' pour terminer] : ")
    
    return auto

#1.3.2

def lirelettre(T, E, a):
    setEtats = set()
    for transition in T:
        if transition[0] in E and transition[1] == a:
            setEtats.add(transition[2])
    return list(setEtats)

#1.3.3

def liremotRec(T, e, mot, etape):
    if etape == len(mot):
        return e
    for t in T:
        if t[0] == e and t[1] == mot[etape]:
            return liremotRec(T, t[2], mot, etape+1)

def liremot(T, E, m):
    setResultat = set()
    for e in E:
        setResultat.add(liremotRec(T, e, m, 0))
    if None in setResultat:
        setResultat.remove(None)
    return list(setResultat)

#1.3.4

def accepteRec(A, e, mot, etape):
    if etape == len(mot) and e in A["F"]:
        return True
    elif etape >= len(mot):
        return False
    for t in A["transitions"]:
        if t[0] == e and t[1] == mot[etape]:
            return accepteRec(A, t[2], mot, etape+1)

def accepte(A, mot):
    for e in A["I"]:
        if accepteRec(A, e, mot, 0):
            return True
    return False

#1.3.5

def langage_accept(A, n):
    setResultat = set()
    L = tousmots(A["alphabet"], n-1)
    for mot in L:
        if accepte(A, mot):
            setResultat.add(mot)
    return list(setResultat)

#1.3.6 - Car des langages peuvent avoir un nombre infini de mots

if __name__ == "__main__":
    print(pref("coucou"))
    print(suf("coucou"))
    print(fact("coucou"))
    print(miroir("coucou"))
    print(concatene(L1,L2))
    print(puis(L3,2))
    print(tousmots(['a','b'], 3))
    print(lirelettre(auto["transitions"],auto["etats"],'a'))
    print(liremot(auto["transitions"],auto["etats"],'aba'))
    print(accepte(auto, "aba"))
    print(langage_accept(auto, 5))
    
    autoD = defauto()
    print(autoD)