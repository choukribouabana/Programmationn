

# Cette fonction calcule le nombre d'occurence de chaque symbole sortant
def construireOcc(ll):
    occ = dict()
    # On parcourt le vecteur L symbol par symbol
    for symbol in ll:
        # Si on a un symbol sortant
        if symbol != "$" and symbol != 1:
            # On incrémente son nombre d'occurence
            try:
                occ[symbol] += 1
            # Sinon si c'est le premier symbol, on lui affecte 1
            except KeyError:
                occ[symbol] = 1
    return occ

# Cette fonction calcule la position du premier noeud préfixé par un symbol
# on a pas besoin de listedesnoeuds pour construire F
def construireF(occ, ll):
    f = dict()
    # On trie les symbols
    sortedKeys = sorted(occ.keys())
    # Le premier symbol correspond toujours au premier noeud
    f[sortedKeys[0]] = 1
    # Pour chaque symbol, la position du premier noeud préfixé par lui égale
    # la position du précédent noeud préfixé + le nombre d'occurence du symbol
    for i in range(1, len(sortedKeys)):
        f[sortedKeys[i]] = f[sortedKeys[i-1]] + occ[sortedKeys[i-1]]
    return f


def select(caractère, chaine, jème):
    # Retourne l'indice du jème caractère dans la chaine en réelle
    return [i for i, n in enumerate(chaine) if n == caractère][jème - 1]


def rank(caractère, chaine, fin):
    # Retourne le nombre d'occurence du caractère de la chaine[0:fin]
    return chaine[0:fin + 1].count(caractère)