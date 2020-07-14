from . import Fonctions

def trouverLePlusLongSuffixe(indiceNoeud, chaineDesParentheses):
    resultat = 0
    # On trouve la position du noeud dans la chaine des parenthèses
    indiceNoeudDansCDP = Fonctions.select("(", chaineDesParentheses, indiceNoeud + 1)
    # On parcours la chaine en démarrant de indiceNoeudDansCDP de gauche à droite
    # jusqu'à ce que le résultat égale 1
    while resultat != 1:
        # On décrémente l'indice à chaque itération
        indiceNoeudDansCDP -= 1
        # Si on rencontre lors de notre parcours une ")" on décrémente le résultat de 1
        if chaineDesParentheses[indiceNoeudDansCDP] == ")":
            resultat -= 1
        # Sinon si on lis un "(" on incrémente le résultat
        else:
            resultat += 1
    # On retourne l'indice du plus long préfixe
    return Fonctions.rank("(", chaineDesParentheses, indiceNoeudDansCDP - 1)

def noeudSuivant(indiceNoeudCourant, symboleSortant, f, ll):
    # Si le noeud courant n'est pas la racine
    if indiceNoeudCourant != 0:
        # On détérmine l'indice du indiceNoeudCourant ième 1 dans le vecteur Ll
        indice1 = Fonctions.select(1, ll, indiceNoeudCourant)
        # Puis on calcule le nombre d'occurence de symboleSortant dans le vecteur ll[0:indice1]
        nbOcc = Fonctions.rank(symboleSortant, ll, indice1)
        # Finalement on trouve l'indice du premier noeud préfixé par symboleSortant
        # retourne l'indice réelle
        return f[symboleSortant] + nbOcc
    # Sinon si le noeud courant est bien la racine
    else:
        # On retourne directement l'indice du symboleSortant dans la listeDesNoeuds
        # Au lieu d'utiliser la fonction C car index() est plus rapide
        return f[symboleSortant]