# Cette fonction retourne la table des suffixes
def suffixArray(chaineOriginale, LongChaineOriginale):
    # On calcule tous les suffixes et leurs indices
    # Puis On garde les indices seulement
    return [indice for rotation, indice in sorted((chaineOriginale[i:], i) for i in range(LongChaineOriginale))]


# Cette fonction calcule la bwt
def calculerBwt(suffixArr, chaineOriginale):
    bwt = str()
    # On parcours la table des suffixes
    for sa in suffixArr:
        # Si l'indice == 0, on ajoute le caractère de fin "$"
        if sa == 0:
            bwt += "$"
        # Sinon, on ajoute le caractère qui précéde l'indice [sa] dans la chaine Originale.
        else:
            bwt += chaineOriginale[sa - 1]
    return bwt