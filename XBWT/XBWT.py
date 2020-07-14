from . import Fonctions

def calculerRcpLcp(longChaineOriginale, chaineOriginale, suffixArr):
    lcp, rcp = list(), list()
    # Le nombre de parcours égale la longueur de la chaine originale
    for i in range(longChaineOriginale-1):
        nbCarCommunsRcp = 0
        nbCarCommunsLcp = 0
        fin = False
        k = suffixArr[i]
        j = suffixArr[i+1]
        # On compare entre chaque deux suffixes consécutives
        while k < longChaineOriginale and j < longChaineOriginale :
            if chaineOriginale[k] == chaineOriginale[j] :
                # la RCP
                # Si fin = True, on arrête la comparaison pour le vecteur MR
                if chaineOriginale[k] != "$" and fin ==False :
                    nbCarCommunsRcp += 1
                else:
                    fin = True
                # La LCP
                nbCarCommunsLcp += 1
                k += 1
                j += 1
            else:
                break
        lcp.append(nbCarCommunsLcp)
        rcp.append(nbCarCommunsRcp)
    return rcp, lcp

def calculerMr(longChaineOriginale, rcp, lcp):
    mr = list()
    # Le premier élément est toujours un 1
    mr.append(1)
    # On remplit le vecteur mr en comparant les vecteurs LCP et RCP
    for i in range(longChaineOriginale - 1):
        if (lcp[i] > rcp[i]):
            mr.append(0)
        else:
            mr.append(1)
    return mr


def calculerXbwt(mr, longChaineOriginale, bwt):
    ll, listeDesCar = list(), list()
    debut = 0

    for i in range(1, longChaineOriginale + 1):
        # Si on a atteint le dernier élément ou le début de la portée maximale
        if i == longChaineOriginale or mr[i] == 1:
            # On copie les caractères distincts correspondant dans la chaine bwt
            listeDesCar = list(dict.fromkeys(bwt[debut:i]))
            # Le début de la prochaine portée maximale est l'élément actuelle
            debut = i
            # On ajoute les symboles triées léxicographiquemet au vecteur ll
            ll.extend(sorted(listeDesCar))
            # Le dernier caractère lui correspond un 1
            ll.append(1)
    return ll


def calculerP(rcp, mr, longChaineOriginale, chaineOriginale, suffixArr):
    pile = list()
    chaineDesParentheses = str()
    # On ajoute d'abord la racine à la pile
    pile.append((0, -1))
    # On enpile la parenthèse ouvrante correspondante
    chaineDesParentheses += "("
    # On parcours le vecteur mr
    for i in range(1, longChaineOriginale):
        # Si l'élément courant est le début de la portée maximale
        if mr[i] == 1:
            # on sauvegarde le rcp correspondant
            rcpCourant = rcp[i - 1]
            # Si le rcp du dernier élément dans la pile est supérieur ou égale au rcp de l'élément courant
            while pile[-1][1] >= rcpCourant:
                # On défile ce dernier élement de la pile
                pile.pop()
                # Et on insére une parenthèse fermante
                chaineDesParentheses += ")"
            # Au cas ou la condition précédente n'élimine pas tous les préfixes
            # On vérifie si le Lcp de l'élement courant est supérieur au rcp
            if chaineOriginale[suffixArr[pile[-1][0]] + rcpCourant] != "$":
                rcpCourant = pile[-1][1]
                pile.pop()
                chaineDesParentheses += ")"
            # On enpile l'élément courant
            pile.append((i, rcpCourant))
            # On insére une parenthèse ouvrante
            chaineDesParentheses += "("
    # Tant que la pile n'est pas vide
    while pile:
        # On dépile
        pile.pop()
        # On ferme la parenthèse
        chaineDesParentheses += ")"
    return chaineDesParentheses

def construireListeDesNoeudsFinaux(ll, listeDesNoeuds):
    longMotifs = len(listeDesNoeuds)
    dictDesNoeuds = dict()
    # On stocke les indices des premiers noeuds préfixés par chaque symbole de l'alphabet
    for i in range(longMotifs):
        # On trouve les noeuds finaux
        posDollar = Fonctions.select("$", ll, i+1)
        # On calcule l'indice correspondant à ce noeud final
        nb1 = Fonctions.rank(1, ll, posDollar)
        # On l'ajoute au dictionnaire
        dictDesNoeuds[nb1] = listeDesNoeuds[i]
    return dictDesNoeuds